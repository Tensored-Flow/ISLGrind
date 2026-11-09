import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("import_apmo", ROOT / "import_apmo.py")
apmo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(apmo)


class APMOImportTests(unittest.TestCase):
    def setUp(self):
        self.papers = json.loads((ROOT / "apmo_problems.json").read_text(encoding="utf-8"))["papers"]

    def test_official_archive_discovery_ignores_solutions_and_external_links(self):
        html = '''<a href="/static/problems/apmo1989_prb.pdf">1989</a>
        <a href="https://apmo-official.org/static/problems/apmo2026_prb.pdf">2026</a>
        <a href="/static/problems/apmo1989_prb.pdf">Duplicate</a>
        <a href="/static/solutions/apmo2026_sol.pdf">Solutions</a>
        <a href="https://example.com/static/problems/apmo2027_prb.pdf">Other</a>'''
        self.assertEqual(apmo.archive_years(html), [1989, 2026])
        with self.assertRaises(ValueError):
            apmo.archive_years("<html>Maintenance</html>")

    def test_generated_bank_is_reproducible(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "bank.js"
            apmo.write_bank(output, apmo.build_records(self.papers))
            self.assertEqual(output.read_bytes(), (ROOT / "bank_apmo.js").read_bytes())

    def test_incomplete_or_duplicate_paper_is_rejected(self):
        for numbers in ([1, 2, 3, 4], [1, 2, 3, 4, 4]):
            papers = copy.deepcopy(self.papers)
            papers[0]["problems"] = papers[0]["problems"][:len(numbers)]
            for problem, number in zip(papers[0]["problems"], numbers):
                problem["number"] = number
            with self.assertRaisesRegex(ValueError, "1 through 5"):
                apmo.build_records(papers)

    def test_missing_year_duplicate_id_and_answer_leak_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "every year"):
            apmo.build_records(self.papers[:1] + self.papers[2:])
        papers = copy.deepcopy(self.papers)
        papers[1]["problems"][0]["id"] = papers[0]["problems"][0]["id"]
        with self.assertRaisesRegex(ValueError, "duplicate"):
            apmo.build_records(papers)
        papers = copy.deepcopy(self.papers)
        papers[0]["problems"][0]["body"] += "\nAnswer: 51"
        with self.assertRaisesRegex(ValueError, "without an answer"):
            apmo.build_records(papers)

    def test_refresh_downloads_the_official_pdf_and_checks_reviewed_hash(self):
        pdf = b"%PDF-1.4\nreviewed fixture"
        paper = {"year": 1989, "sha256": hashlib.sha256(pdf).hexdigest()}
        archive = b'<a href="/static/problems/apmo1989_prb.pdf">1989</a>'
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(apmo, "download", side_effect=[archive, pdf]) as fetch:
                apmo.refresh_sources([paper], Path(directory))
            self.assertEqual(fetch.call_args_list[0].args, (apmo.ARCHIVE_URL,))
            self.assertEqual(fetch.call_args_list[1].args, (apmo.paper_url(1989),))
            self.assertEqual((Path(directory) / "apmo1989_prb.pdf").read_bytes(), pdf)

    def test_new_or_changed_paper_requires_review_and_does_not_replace_bank(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "bank.js"
            output.write_text("previous bank", encoding="utf-8")
            for year in (1989, 2027):
                archive = f'<a href="/static/problems/apmo{year}_prb.pdf">{year}</a>'.encode()
                with self.subTest(year=year), patch("sys.argv", [
                    "import_apmo.py", "--refresh", "--cache-dir", directory, "--output", str(output)
                ]):
                    with patch.object(apmo, "download", side_effect=[archive, b"%PDF-new content"]):
                        with self.assertRaisesRegex(ValueError, "need review"):
                            apmo.main()
                self.assertEqual(output.read_text(encoding="utf-8"), "previous bank")

    def test_refresh_rejects_non_pdf_responses(self):
        archive = b'<a href="/static/problems/apmo1989_prb.pdf">1989</a>'
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(apmo, "download", side_effect=[archive, b"<html>Error</html>"]):
                with self.assertRaisesRegex(ValueError, "not a PDF"):
                    apmo.refresh_sources(self.papers, Path(directory))


if __name__ == "__main__":
    unittest.main()
