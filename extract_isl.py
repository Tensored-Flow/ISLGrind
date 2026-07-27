#!/usr/bin/env python3
"""
Split the official IMO Shortlist PDFs (2006-latest) into individual problems.

Output layout:
    ISL_problems/
        2024/A1.txt ... N8.txt
        2024/_problems.md          (all problems for the year, one page)
        ...
        index.json                 (machine-readable: year, code, category, country, text)
        index.md                   (human index, links to every problem)

Two PDF layouts are handled by one rule:
  * a problem statement starts at a line matching  ^[ACGN]<n>.
  * it ends at the next such marker OR a "Solution" line, whichever comes first.
  * only the FIRST occurrence of each code is kept (drops duplicate markers that
    reappear in the solutions section of "consolidated" years).

Some years (2010, 2013-15, 2017-25) embed math in a font whose ToUnicode map is
broken, so operators extract as wrong glyphs. GLYPH_FIX recovers the common ones.
Subscripts/superscripts/fractions still flatten -- those statements are marked
fidelity="approx" in index.json.
"""
import json, re, subprocess, sys
from collections import Counter
from pathlib import Path

SRC = Path("IMO_Shortlists")
OUT = Path("ISL_problems")
CATEGORY = {"A": "Algebra", "C": "Combinatorics", "G": "Geometry", "N": "Number Theory"}

# wrong-glyph -> intended symbol, for the broken-font years
GLYPH_FIX = {
    "“": "=", "”": "=",      # “ ” -> =
    "`": "+",                            # ` -> +
    "´": "−",                 # ´ -> − (minus)
    "¨": "·",                 # ¨ -> · (cdot)
    "ă": "<", "ą": ">",       # ă > , ą <  ... (set below precisely)
    "ď": "≤", "ě": "≥",  # ď -> ≤ , ě -> ≥
    "Ñ": "→",                 # Ñ -> →
}
# precise relational glyphs confirmed from samples
GLYPH_FIX["ă"] = "<"   # ă -> <
GLYPH_FIX["ą"] = ">"   # ą -> >

GARBLED_YEARS = {2010, 2013, 2014, 2015, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025}

SOLUTION = re.compile(r"^\s*Solution\b")
COUNTRY = re.compile(r"\(([A-Z][A-Za-z .'\-]+)\)")
# a line that is *only* a problem code, optionally "CODE  XYZ  (Country)"
BARE_CODE = re.compile(r"^\s*[ACGN]\d{1,2}(\s+[A-Z]{2,4}\s+\(.+\))?\s*$")


def marker_code(ln):
    """Return 'A1' etc. if this line starts a problem statement, across the 4
    layouts seen in 2006-2024; else None.  Running headers (which repeat the
    code alongside the year/'Shortlist') are rejected."""
    s = ln.strip()
    if not s or "IMO" in s or "hortlist" in s:
        return None
    m = re.match(r"([ACGN])(\d{1,2})(\.)?", s)
    if not m:
        return None
    code = m.group(1) + m.group(2)
    indent = len(ln) - len(ln.lstrip())
    if m.group(3) == ".":                       # "A1. <statement>"  (most years)
        return code if indent <= 8 else None
    rest = s[m.end():].strip()                   # no period: 2009/2011 styles
    if indent > 3:                               # right-aligned header copy
        return None
    if rest == "":                               # "A1" alone           (2011)
        return code
    if re.match(r"^[A-Z]{2,4}\s+\(.+\)$", rest): # "A1  CZE  (Czech…)"  (2009)
        return code
    return None


def pdftext(path):
    return subprocess.run(
        ["pdftotext", "-layout", str(path), "-"],
        capture_output=True, text=True
    ).stdout


def strip_running_headers(lines):
    """Drop page numbers and any short line that repeats often (running headers)."""
    norm = [ln.strip() for ln in lines]
    freq = Counter(l for l in norm if l)
    out = []
    for raw, l in zip(lines, norm):
        if re.fullmatch(r"\d{1,3}", l):                      # bare page number
            continue
        if l and len(l) < 80 and freq[l] >= 4:               # repeating header/footer
            continue
        if re.fullmatch(r"(Algebra|Combinatorics|Geometry|Number Theory)", l):
            continue
        out.append(raw)
    return out


def clean(text, garbled):
    if garbled:
        for bad, good in GLYPH_FIX.items():
            text = text.replace(bad, good)
        text = re.sub(r"·( ·)+", "···", text)  # · · · -> ···
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_year(pdf):
    year = int(re.search(r"(\d{4})", pdf.name).group(1))
    garbled = year in GARBLED_YEARS
    lines = strip_running_headers(pdftext(pdf).splitlines())

    # locate first occurrence of each problem code
    marks = []           # (line_idx, code)
    seen = set()
    for i, ln in enumerate(lines):
        code = marker_code(ln)
        if code and code not in seen:
            seen.add(code)
            marks.append((i, code))

    problems = []
    for j, (start, code) in enumerate(marks):
        end = marks[j + 1][0] if j + 1 < len(marks) else len(lines)
        # cut at first Solution line inside the block (interleaved layout)
        for k in range(start + 1, end):
            if SOLUTION.match(lines[k]):
                end = k
                break
        block = lines[start:end]
        # country: from the marker/first lines (2009) or trailing parens (2024)
        country = None
        cm = COUNTRY.search("\n".join(block[:2]) or "") or COUNTRY.search("\n".join(block))
        if cm:
            country = cm.group(1).strip()
        # drop leading lines that are just the code (2011) or code+country (2009)
        while block and BARE_CODE.match(block[0]):
            block.pop(0)
        body = clean("\n".join(block), garbled)
        body = re.sub(r"^\s*[ACGN]\d{1,2}\.\s*", "", body)   # drop leading "A1." label
        problems.append({
            "year": year, "code": code, "category": CATEGORY[code[0]],
            "country": country, "fidelity": "approx" if garbled else "exact",
            "text": body,
        })
    # natural sort: A1,A2..A10,C1...
    problems.sort(key=lambda p: (p["code"][0], int(p["code"][1:])))
    return year, garbled, problems


def main():
    pdfs = sorted(SRC.glob("ISL-*.pdf"))
    OUT.mkdir(exist_ok=True)
    index = []
    md = ["# IMO Shortlist — individual problems\n"]
    for pdf in pdfs:
        year, garbled, problems = extract_year(pdf)
        ydir = OUT / str(year)
        ydir.mkdir(exist_ok=True)
        for p in problems:
            (ydir / f"{p['code']}.txt").write_text(p["text"] + "\n")
            index.append(p)
        # per-year combined markdown
        ymd = [f"# IMO Shortlist {year} problems",
               f"_fidelity: {'approx (math glyphs recovered best-effort)' if garbled else 'exact'}_\n"]
        for p in problems:
            ymd.append(f"## {p['code']} — {p['category']}"
                       + (f"  ({p['country']})" if p['country'] else ""))
            ymd.append("\n```\n" + p["text"] + "\n```\n")
        (ydir / "_problems.md").write_text("\n".join(ymd))
        flag = " ⚠ approx-math" if garbled else ""
        md.append(f"- **{year}** — {len(problems)} problems{flag} "
                  f"([all]({year}/_problems.md))")
        print(f"{year}: {len(problems):3d} problems"
              f"  ({'approx' if garbled else 'exact'} math)")

    (OUT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1))
    (OUT / "index.md").write_text("\n".join(md) + "\n")
    print(f"\nTotal: {len(index)} problems across {len(pdfs)} years -> {OUT}/")


if __name__ == "__main__":
    main()
