#!/usr/bin/env python3
"""
Ingest the compendium vision-workflow output (/tmp/comp_out/<year>-pNNN.json)
into ISL_problems/<year>/<CODE>.tex.

Coded years keep their printed code (A1, G7, ...). Codeless years (1990-93,
1997, 1998) get a synthetic code: within each (year, subject), problems are
ordered by their printed list number and indexed A1,A2,.../C1,... so the
trainer's difficulty model (level = within-subject index) still applies.
"""
import json, re, glob
from pathlib import Path
from collections import defaultdict

PROB = Path(__file__).parent / "ISL_problems"
SUBJ_LETTER = {"Algebra": "A", "Combinatorics": "C", "Geometry": "G", "Number Theory": "N"}


def main():
    by_year = defaultdict(list)   # year -> list of problem dicts (deduped by number)
    seen = defaultdict(dict)      # year -> {number: problem}
    for f in sorted(glob.glob("/tmp/comp_out/*.json")):
        m = re.search(r"(\d{4})-p", f)
        if not m:
            continue
        year = int(m.group(1))
        try:
            data = json.load(open(f))
        except Exception:
            continue
        problems = data.get("problems", data) if isinstance(data, dict) else data
        for p in problems:
            num = p.get("number")
            latex = (p.get("latex") or "").strip()
            if num is None or not latex:
                continue
            prev = seen[year].get(num)
            if prev is None or len(latex) > len(prev.get("latex", "")):
                seen[year][num] = p

    written = 0
    for year, probs in seen.items():
        plist = sorted(probs.values(), key=lambda p: p["number"])
        # assign codes
        subj_counter = defaultdict(int)
        ydir = PROB / str(year)
        ydir.mkdir(parents=True, exist_ok=True)
        used = set()
        for p in plist:
            code = (p.get("code") or "").strip().replace(" ", "")
            if not re.fullmatch(r"[ACGN]\d{1,2}", code):
                letter = SUBJ_LETTER.get(p["subject"])
                if not letter:
                    continue
                subj_counter[letter] += 1
                code = f"{letter}{subj_counter[letter]}"
            else:
                # keep printed code, but track counter so synthetic ones don't collide
                subj_counter[code[0]] = max(subj_counter[code[0]], int(code[1:]))
            if code in used:
                continue
            used.add(code)
            cc = p.get("country")
            head = f"% country: {cc}\n" if cc else ""
            (ydir / f"{code}.tex").write_text(head + p["latex"].strip() + "\n")
            written += 1
        print(f"{year}: {len(plist)} problems -> codes {sorted(used, key=lambda c:(c[0],int(c[1:])))}")
    print(f"\ningested {written} compendium problems (1990-2004)")


if __name__ == "__main__":
    main()
