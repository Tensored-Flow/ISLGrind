#!/usr/bin/env python3
"""
Build the trainer's problem bank from all extracted ISL problems.

Sources (in priority order per problem):
  ISL_problems/<year>/<CODE>.tex   -> clean LaTeX  (format: "latex")
  ISL_problems/<year>/<CODE>.txt   -> faithful text (format: "text")

Also ingests the vision-workflow output (/tmp/isl_out/<year>-pNNN.json)
into <year>/<CODE>.tex first, so garbled years become LaTeX.

Difficulty model: a problem's within-subject index IS the ISL difficulty
ordering (A1 easiest ... A8 hardest), so level = that index (1-8).

Output: app/bank.js  ->  window.ISL_BANK = [ {id, year, code, subject,
level, country, format, body}, ... ]
"""
import json, re, glob
from pathlib import Path

ROOT = Path(__file__).parent
PROB = ROOT / "ISL_problems"
SUBJECT = {"A": "Algebra", "C": "Combinatorics", "G": "Geometry", "N": "Number Theory"}


def ingest_workflow():
    """Pull /tmp/isl_out/*.json (verified vision output) into ISL_problems/<year>/<code>.tex"""
    n = 0
    for f in glob.glob("/tmp/isl_out/*.json"):
        m = re.search(r"(\d{4})-p", f)
        if not m:
            continue
        year = m.group(1)
        try:
            data = json.load(open(f))
        except Exception:
            continue
        problems = data.get("problems", data) if isinstance(data, dict) else data
        ydir = PROB / year
        ydir.mkdir(parents=True, exist_ok=True)
        for p in problems:
            code = p.get("code", "").strip().replace(" ", "")
            latex = (p.get("latex") or "").strip()
            if not re.fullmatch(r"[ACGN]\d{1,2}", code) or not latex:
                continue
            dest = ydir / f"{code}.tex"
            # keep first/most complete: don't overwrite a longer existing tex
            if dest.exists() and len(dest.read_text()) >= len(latex):
                continue
            cc = p.get("country")
            head = f"% country: {cc}\n" if cc else ""
            dest.write_text(head + latex + "\n")
            n += 1
    print(f"ingested {n} workflow problems into ISL_problems/")


def load_country_tex(text):
    cc = None
    m = re.match(r"%\s*country:\s*(.+)", text)
    if m:
        cc = m.group(1).strip()
        text = text[m.end():].lstrip("\n")
    return cc, text


def build():
    bank = []
    for ydir in sorted(PROB.glob("[0-9][0-9][0-9][0-9]")):
        year = int(ydir.name)
        codes = {}
        for p in ydir.glob("*.tex"):
            codes[p.stem] = ("latex", p)
        for p in ydir.glob("*.txt"):
            codes.setdefault(p.stem, ("text", p))   # .tex wins
        for code, (fmt, path) in codes.items():
            if not re.fullmatch(r"[ACGN]\d{1,2}", code):
                continue
            body = path.read_text().strip()
            country = None
            if fmt == "latex":
                country, body = load_country_tex(body)
            bank.append({
                "id": f"{year}-{code}",
                "year": year, "code": code,
                "subject": SUBJECT[code[0]],
                "level": int(code[1:]),
                "country": country,
                "format": fmt,
                "body": body,
            })
    bank.sort(key=lambda p: (p["level"], p["year"], p["code"]))
    out = ROOT / "bank.js"
    out.write_text("window.ISL_BANK = " + json.dumps(bank, ensure_ascii=False) + ";\n")
    # Keep the browsable machine index in lockstep with the trainer bank.
    (PROB / "index.json").write_text(
        json.dumps(bank, ensure_ascii=False, indent=1) + "\n"
    )
    # stats
    from collections import Counter
    lv = Counter(p["level"] for p in bank)
    fm = Counter(p["format"] for p in bank)
    print(f"bank: {len(bank)} problems -> {out}")
    print("  by level:", dict(sorted(lv.items())))
    print("  by format:", dict(fm))
    print("  years:", min(p['year'] for p in bank), "-", max(p['year'] for p in bank))


if __name__ == "__main__":
    ingest_workflow()
    build()
