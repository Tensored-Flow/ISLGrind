#!/usr/bin/env python3
"""Build the senior Balkan Mathematical Olympiad problem bank (1984-present).

The importer uses the John Scholes HTML archive for 1984-2003 and the open
AI-MO olympiad Markdown corpus for 2008-2025.  The four 2004-2007 papers fill
the archive gap from the Balkan MO compendium, and the 2026 statements come
from the official host paper.  Only problem statements are emitted.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import textwrap
from pathlib import Path


SUBJECTS = {
    "A": "Algebra",
    "C": "Combinatorics",
    "G": "Geometry",
    "N": "Number Theory",
}

# One topic letter per problem, in paper order.  Balkan MO papers do not label
# topics themselves, so these are editorial classifications used by ISLGrind.
TOPICS = {
    1984: "AGNA", 1985: "GANC", 1986: "GGNG", 1987: "AAGG",
    1988: "GAGN", 1989: "NNGC", 1990: "NAGC", 1991: "GNGN",
    1992: "NAGC", 1993: "ACGN", 1994: "GNCC", 1995: "AGNC",
    1996: "GNGC", 1997: "GCGA", 1998: "NAGN", 1999: "GNGC",
    2000: "AGCN", 2001: "NGAC", 2002: "CNGA", 2003: "NGAG",
    2004: "ANGC", 2005: "GNAC", 2006: "AGNN", 2007: "GANC",
    2008: "GACN", 2009: "NGCA", 2010: "AGGN", 2011: "GACG",
    2012: "GACN", 2013: "GNAC", 2014: "ANGC", 2015: "AGCN",
    2016: "AGNC", 2017: "NGNC", 2018: "GACN", 2019: "NAGC",
    2020: "GNCN", 2021: "GANC", 2022: "GNAC", 2023: "AGNC",
    2024: "GCNA", 2025: "CGAC", 2026: "ACGA",
}

MARKDOWN_FILES = {
    2008: "en-2008-BMO-type1.md", 2009: "en-2009-BMO-type2.md",
    2010: "en-2010-BMO-type2.md", 2011: "en-2011-BMO-type1.md",
    2012: "en-2012-BMO-type3.md", 2013: "en-2013-BMO-type2.md",
    2014: "en-2014-BMO-type1.md", 2015: "en-2015-BMO-type1.md",
    2016: "en-2016-BMO-type1.md", 2017: "en-2017-BMO-type3.md",
    2018: "en-2018-BMO-type3.md", 2019: "en-2019-BMO-type1.md",
    2020: "en-2020-BMO-type1.md", 2021: "en-2021-BMO-type1.md",
    2022: "en-2022-BMO-type1.md", 2023: "en-2023-BMO-type1.md",
    2024: "en-2024-BMO-type1.md", 2025: "en-2025-BMO-type1.md",
}

COMPENDIUM_URL = "https://www.toomates.net/biblioteca/CompendiumBalkanMO.pdf"
OFFICIAL_2025_URL = (
    "https://bmo2025.pmf.unsa.ba/wp-content/uploads/2025/05/"
    "Problems%20-%20Solutions.pdf"
)
OFFICIAL_2026_URL = (
    "https://hms.gr/43bmo2026/pdf/"
    "BMO2026_Problems_All_Languages_Country_Order.pdf"
)
HF_BASE = (
    "https://huggingface.co/datasets/AI-MO/olympiads/blob/"
    "a9b779cddef3b7fa998032849a6a0980855db5f9/Balkan_MO/md/"
)


MANUAL_STATEMENTS = {
    2004: [
        r"""The sequence $\{a_n\}_{n\geq 0}$ of real numbers satisfies
        \[a_{m+n}+a_{m-n}-m+n-1=\frac{1}{2}(a_{2m}+a_{2n})\]
        for all non-negative integers $m$ and $n$ with $m\geq n$. If $a_1=3$, determine $a_{2004}$.""",
        r"""Solve in prime numbers the equation
        \[x^y-y^x=xy^2-19.\]""",
        r"""Let $O$ be an interior point of an acute triangle $ABC$. The circles with centers at the midpoints of its sides and passing through $O$ meet for a second time at the points $K,L,M$, respectively, all different from $O$. Prove that $O$ is the incenter of triangle $KLM$ if and only if $O$ is the circumcenter of triangle $ABC$.""",
        r"""The plane is partitioned into regions by a finite number of lines, no three of which are concurrent. Two regions are called neighbors if the intersection of their boundaries is a segment, a ray, or a line. An integer is assigned to each region so that:

        (i) the product of the integers assigned to any two neighboring regions is less than their sum;

        (ii) for each given line and each half-plane determined by it, the sum of the integers assigned to all regions in that half-plane is zero.

        Prove that this is possible if and only if not all the lines are parallel.""",
    ],
    2005: [
        r"""The incircle of an acute triangle $ABC$ touches $AB$ and $AC$ at $D$ and $E$, respectively. The bisectors of $\angle ACB$ and $\angle ABC$ meet the line $DE$ at $X$ and $Y$, respectively, and $Z$ is the midpoint of $BC$. Prove that triangle $XYZ$ is equilateral if and only if $\angle A=60^\circ$.""",
        r"""Find all primes $p$ such that $p^2-p+1$ is a perfect cube.""",
        r"""Let $a,b,c$ be positive real numbers. Prove that
        \[\frac{a^2}{b}+\frac{b^2}{c}+\frac{c^2}{a}\geq a+b+c+\frac{4(a-b)^2}{a+b+c}.\]
        When does equality occur?""",
        r"""Let $n\geq 2$ be an integer. Let $S$ be a subset of $\{1,2,\ldots,n\}$ such that $S$ contains neither two elements one of which divides the other, nor two elements which are coprime. What is the maximum possible number of elements of $S$?""",
    ],
    2006: [
        r"""Let $a,b,c$ be positive real numbers. Prove that
        \[\frac{1}{a(b+1)}+\frac{1}{b(c+1)}+\frac{1}{c(a+1)}\geq\frac{3}{1+abc}.\]""",
        r"""Let $ABC$ be a triangle and let $m$ be a line which meets the sides $AB$ and $AC$ at interior points $D$ and $F$, respectively, and the line $BC$ at a point $E$ such that $C$ lies between $B$ and $E$. The lines through $A,B,C$ parallel to $m$ meet the circumcircle of triangle $ABC$ again at $A_1,B_1,C_1$, respectively. Prove that $A_1E,B_1F,C_1D$ are concurrent.""",
        r"""Find all triples of positive rational numbers $(m,n,p)$ such that
        \[m+\frac{1}{np},\qquad n+\frac{1}{pm},\qquad p+\frac{1}{mn}\]
        are integers.""",
        r"""Let $m$ be a positive integer and let $\{a_n\}_{n\geq0}$ be defined by $a_0=a\in\mathbb N$ and
        \[a_{n+1}=\begin{cases}a_n/2,&a_n\text{ is even},\\a_n+m,&a_n\text{ is odd}.
        \end{cases}\]
        Find all positive integers $a$ for which the sequence is periodic from the beginning.""",
    ],
    2007: [
        r"""Let $ABCD$ be a convex quadrilateral with $AB=BC=CD$ and $AC\ne BD$, and let $E$ be the intersection of its diagonals. Prove that $AE=DE$ if and only if $\angle BAD+\angle ADC=120^\circ$.""",
        r"""Find all functions $f:\mathbb R\to\mathbb R$ such that, for all real numbers $x,y$,
        \[f(f(x)+y)=f(f(x)-y)+4f(x)y.\]""",
        r"""Determine all positive integers $n$ for which there exists a permutation $\sigma$ of $\{1,2,\ldots,n\}$ such that
        \[\sqrt{\sigma(1)+\sqrt{\sigma(2)+\cdots+\sqrt{\sigma(n)}}}\]
        is rational.""",
        r"""Let $n\geq3$ be an integer. Let $C_1,C_2,C_3$ be the boundaries of three convex $n$-gons in the plane such that the intersection of any two is a finite set. Find the maximum possible number of points in $C_1\cap C_2\cap C_3$.""",
    ],
    2026: [
        r"""A set $S$ of positive real numbers is called Aristotelian if, for any $x,y,z\in S$ with $x<y<z$, the number
        \[\frac{z-x}{y}\]
        also belongs to $S$. Find all integers $n\geq4$ for which there exists an Aristotelian set with exactly $n$ elements.""",
        r"""Let $n$ be a positive integer. A $2n\times2n$ board is tiled with $2\times1$ and $1\times2$ dominoes. A pivot of a domino consists of selecting one of its squares and rotating the whole domino by $90^\circ$ clockwise, $90^\circ$ counterclockwise, or $180^\circ$ about the center of that square. Prove that it is possible to pivot all the dominoes simultaneously so that they still tile the board.""",
        r"""Let $ABCD$ be a parallelogram such that $\angle DAB<90^\circ$ and $AB<AD$. Let $H$ be the orthocenter of triangle $BCD$, and let $H'$ be the reflection of $H$ across $BD$. The line $AH$ meets $BD,CD,BC$ at $E,F,G$, respectively. Prove that the circumcircles of triangles $HEH'$ and $CFG$ are tangent.""",
        r"""Let $n\geq2$. Initially, $n$ copies of the number $1$ are written on a blackboard. In one operation, choose two numbers $a,b$, not both zero, erase them, and write
        \[\frac{(a-b)^2}{a+b}\qquad\text{and}\qquad\frac{4ab}{a+b}.\]
        Determine all $n$ for which the number $n$ can appear on the blackboard after finitely many operations.""",
    ],
}


def compact(value: str) -> str:
    """Dedent editorial text while retaining intentional paragraph breaks."""
    value = textwrap.dedent(value).strip()
    paragraphs = re.split(r"\n\s*\n", value)
    return "\n\n".join(re.sub(r"\s*\n\s*", " ", p).strip() for p in paragraphs)


SUBSCRIPT = str.maketrans("0123456789+-=()", "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎")
SUPERSCRIPT = str.maketrans("0123456789+-=()mn", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ᵐⁿ")


def old_html_statement(fragment: str) -> str:
    fragment = re.sub(r"<br\s*/?>", "\n", fragment, flags=re.I)
    fragment = re.sub(
        r"<sub>(.*?)</sub>",
        lambda m: html.unescape(m.group(1)).translate(SUBSCRIPT),
        fragment,
        flags=re.I | re.S,
    )
    fragment = re.sub(
        r"<sup>(.*?)</sup>",
        lambda m: html.unescape(m.group(1)).translate(SUPERSCRIPT),
        fragment,
        flags=re.I | re.S,
    )
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    fragment = html.unescape(fragment).replace("\xa0", " ")
    lines = [re.sub(r"\s+", " ", line).strip() for line in fragment.splitlines()]
    return "\n".join(line for line in lines if line).strip()


def extract_old_html(path: Path) -> list[str]:
    source = path.read_text(encoding="latin-1")
    matches = re.findall(
        r"<b>\s*A?([1-4])\.\s*</b>\s*(?:&nbsp;)?(.*?)(?=</td>)",
        source,
        flags=re.I | re.S,
    )
    by_number = {int(number): old_html_statement(body) for number, body in matches}
    if sorted(by_number) != [1, 2, 3, 4]:
        raise ValueError(f"expected four problems in {path}, got {sorted(by_number)}")
    return [by_number[number] for number in range(1, 5)]


PROBLEM_MARKER = re.compile(
    r"^(?:#{1,4}\s*)?"
    r"(?:(?:\d{4}[ \t]+BMO|BMO[ \t]+\d{4})[ \t]*[-,][ \t]*)?"
    r"(?:PROBLEM|Problem)[ \t]+([1-4])\.?[ \t]*(.*)$",
    flags=re.M,
)
PLAIN_MARKER = re.compile(r"^([1-4])\.\s+(.*)$", flags=re.M)
SOLUTION_MARKER = re.compile(
    r"^(?:#{1,4}\s*)?(?:SOLUTIONS?|Solutions?|Solution)\b",
    flags=re.M,
)


def clean_markdown(body: str) -> str:
    body = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", body)
    body = body.replace("**", "").replace("__", "")
    body = re.sub(
        r"(?m)^\s*(?:#{1,6}\s*)?(?:Proposed by|Author:).*$", "", body
    )
    body = re.sub(r"(?m)^\s*#{1,6}\s*", "", body)
    body = re.sub(r"^Problem\.[ \t]*", "", body)
    body = re.sub(r"(?m)^\s*-\s+", "• ", body)
    body = re.sub(r";\s*-\s+(a (?:long|short) path)", r";\n\n• \1", body)
    body = re.sub(r"^\\quad\$[ \t]*", "", body)
    body = body.replace(r"\sum_{c y c}", r"\sum_{\mathrm{cyc}}")
    body = body.replace("acute- angled", "acute-angled").replace("two- way", "two-way")
    body = body.replace("\u3002", ".")
    body = re.sub(r"[ \t]+\n", "\n", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def extract_markdown(path: Path) -> list[str]:
    source = path.read_text(encoding="utf-8")
    candidates = list(PROBLEM_MARKER.finditer(source))
    if not all(any(int(match.group(1)) == n for match in candidates) for n in range(1, 5)):
        candidates = list(PLAIN_MARKER.finditer(source))

    selected = []
    for number in range(1, 5):
        choices = [match for match in candidates if int(match.group(1)) == number]
        if not choices:
            raise ValueError(f"missing problem {number} in {path}")
        match = choices[0]
        # Some corpora have a title-only marker immediately followed by the
        # real marker.  Prefer the latter only when nothing lies between them.
        if not match.group(2).strip() and len(choices) > 1:
            between = source[match.end():choices[1].start()].strip()
            if not between and choices[1].group(2).strip():
                match = choices[1]
        selected.append(match)

    statements = []
    for match in selected:
        boundaries = [candidate.start() for candidate in candidates if candidate.start() > match.start()]
        boundaries.extend(candidate.start() for candidate in SOLUTION_MARKER.finditer(source, match.end()))
        end = min(boundaries, default=len(source))
        inline = match.group(2).strip()
        tail = source[match.end():end].strip()
        body = "\n".join(part for part in (inline, tail) if part)
        body = clean_markdown(body)
        if len(body) < 30:
            raise ValueError(f"problem {match.group(1)} in {path} is suspiciously short: {body!r}")
        statements.append(body)
    return statements


def source_url(year: int) -> str:
    if year <= 2003:
        return (
            "https://webee.technion.ac.il/people/aditya/"
            f"www.kalva.demon.co.uk/balkan/balk{year % 100:02d}.html"
        )
    if year <= 2007:
        return COMPENDIUM_URL
    if year == 2025:
        return OFFICIAL_2025_URL
    if year == 2026:
        return OFFICIAL_2026_URL
    return HF_BASE + MARKDOWN_FILES[year]


def build_records(html_dir: Path, markdown_dir: Path) -> list[dict]:
    records = []
    for year in range(1984, 2027):
        if year <= 2003:
            statements = extract_old_html(html_dir / f"islgrind-balk{year % 100:02d}.html")
            statement_format = "text"
        elif year <= 2007 or year == 2026:
            statements = [compact(value) for value in MANUAL_STATEMENTS[year]]
            statement_format = "latex"
        else:
            statements = extract_markdown(markdown_dir / MARKDOWN_FILES[year])
            statement_format = "latex"

        if len(statements) != 4:
            raise ValueError(f"expected four statements for {year}, got {len(statements)}")
        for number, (topic, body) in enumerate(zip(TOPICS[year], statements), start=1):
            records.append({
                "id": f"BALKAN-{year}-{number}",
                "source": "Balkan MO",
                "year": year,
                "code": f"{topic}{number}",
                "subject": SUBJECTS[topic],
                "level": number + 4,
                "country": "",
                "format": statement_format,
                "body": body,
                "url": source_url(year),
            })
    return records


def write_bank(path: Path, records: list[dict]) -> None:
    lines = [
        "/* Senior Balkan Mathematical Olympiad, 1984-2026 (43 papers, 172 problems).",
        "   Historical wording: John Scholes archive; 2004-2007: Balkan MO Compendium;",
        "   2008-2025: AI-MO olympiads corpus; 2026: official host paper. */",
        "window.ISL_BANK = (window.ISL_BANK || []).concat([",
    ]
    lines.extend(
        ("," if index else "") + json.dumps(record, ensure_ascii=False, separators=(",", ":"))
        for index, record in enumerate(records)
    )
    lines.append("]);\n")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--html-dir", type=Path, default=Path("/tmp"))
    parser.add_argument(
        "--markdown-dir", type=Path, default=Path("/tmp/islgrind-aimo-balkan-md")
    )
    parser.add_argument("--output", type=Path, default=Path("bank_balkan.js"))
    args = parser.parse_args()

    records = build_records(args.html_dir, args.markdown_dir)
    if len(records) != 172 or len({record["id"] for record in records}) != 172:
        raise ValueError("Balkan MO bank must contain exactly 172 unique records")
    write_bank(args.output, records)
    print(f"wrote {len(records)} problems to {args.output}")


if __name__ == "__main__":
    main()
