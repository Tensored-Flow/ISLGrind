#!/usr/bin/env python3
"""Build the US Ersatz Math Olympiad problem bank (USEMO 2019-2025).

Statements are transcribed to LaTeX from the official contest papers posted by
the USEMO organizers at https://web.evanchen.cc/usemo.html.  The first USEMO is
labelled 2019 there even though it was sat in May 2020.  USEMO 2026 is held on
24-25 October 2026 and is not included yet.  Only problem statements are emitted.
"""

from __future__ import annotations

import argparse
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

# One topic letter per problem, in paper order.  USEMO papers do not label
# topics themselves, so these are editorial classifications used by ISLGrind.
TOPICS = {
    2019: "GACNCG",
    2020: "NCGAGN",
    2021: "CNGGAC",
    2022: "CAGGNA",
    2023: "NCGGCA",
    2024: "CNGAGC",
    2025: "AGCNCN",
}

# IMO-style difficulty ladder: problems 1/4 easy, 2/5 medium, 3/6 hard.
LEVELS = {1: 4, 2: 6, 3: 8, 4: 4, 5: 6, 6: 8}


def paper_url(year: int) -> str:
    return f"https://web.evanchen.cc/exams/USEMO-{year}.pdf"


STATEMENTS = {
    2019: [
        r"""Let $ABCD$ be a cyclic quadrilateral. A circle centered at $O$ passes through $B$ and $D$ and meets lines $BA$ and $BC$ again at points $E$ and $F$ (distinct from $A$, $B$, $C$). Let $H$ denote the orthocenter of triangle $DEF$. Prove that if lines $AC$, $DO$, $EF$ are concurrent, then triangles $ABC$ and $EHF$ are similar.""",
        r"""Let $\mathbb{Z}[x]$ denote the set of single-variable polynomials in $x$ with integer coefficients. Find all functions $\theta\colon\mathbb{Z}[x]\to\mathbb{Z}[x]$ (i.e. functions taking polynomials to polynomials) such that
        \begin{itemize}
        \item for any polynomials $p,q\in\mathbb{Z}[x]$, $\theta(p+q)=\theta(p)+\theta(q)$;
        \item for any polynomial $p\in\mathbb{Z}[x]$, $p$ has an integer root if and only if $\theta(p)$ does.
        \end{itemize}""",
        r"""Consider an infinite grid $\mathcal{G}$ of unit square cells. A \emph{chessboard polygon} is a simple polygon (i.e. not self-intersecting) whose sides lie along the gridlines of $\mathcal{G}$.

        Nikolai chooses a chessboard polygon $F$ and challenges you to paint some cells of $\mathcal{G}$ green, such that any chessboard polygon congruent to $F$ has at least $1$ green cell but at most $2020$ green cells. Can Nikolai choose $F$ to make your job impossible?""",
        r"""Prove that for any prime $p$, there exists a positive integer $n$ such that
        \[1^n+2^{n-1}+3^{n-2}+\cdots+n^1\equiv 2020\pmod{p}.\]""",
        r"""Let $\mathcal{P}$ be a regular polygon, and let $\mathcal{V}$ be the set of its vertices. Each point in $\mathcal{V}$ is colored red, white, or blue. A subset of $\mathcal{V}$ is \emph{patriotic} if it contains an equal number of points of each color, and a side of $\mathcal{P}$ is \emph{dazzling} if its endpoints are of different colors.

        Suppose that $\mathcal{V}$ is patriotic and the number of dazzling edges of $\mathcal{P}$ is even. Prove that there exists a line, not passing through any point of $\mathcal{V}$, dividing $\mathcal{V}$ into two nonempty patriotic subsets.""",
        r"""Let $ABC$ be an acute scalene triangle with circumcenter $O$ and altitudes $\overline{AD}$, $\overline{BE}$, $\overline{CF}$. Let $X$, $Y$, $Z$ be the midpoints of $\overline{AD}$, $\overline{BE}$, $\overline{CF}$. Lines $AD$ and $YZ$ intersect at $P$, lines $BE$ and $ZX$ intersect at $Q$, and lines $CF$ and $XY$ intersect at $R$.

        Suppose that lines $YZ$ and $BC$ intersect at $A'$, and lines $QR$ and $EF$ intersect at $D'$. Prove that the perpendiculars from $A$, $B$, $C$, $O$ to the lines $QR$, $RP$, $PQ$, $A'D'$, respectively, are concurrent.""",
    ],
    2020: [
        r"""Which positive integers can be written in the form
        \[\frac{\operatorname{lcm}(x,y)+\operatorname{lcm}(y,z)}{\operatorname{lcm}(x,z)}\]
        for positive integers $x$, $y$, $z$?""",
        r"""Calvin and Hobbes play a game. First, Hobbes picks a family $\mathcal{F}$ of subsets of $\{1,2,\ldots,2020\}$, known to both players. Then, Calvin and Hobbes take turns choosing a number from $\{1,2,\ldots,2020\}$ which is not already chosen, with Calvin going first, until all numbers are taken (i.e., each player has $1010$ numbers). Calvin wins if he has chosen all the elements of some member of $\mathcal{F}$, otherwise Hobbes wins. What is the largest possible size of a family $\mathcal{F}$ that Hobbes could pick while still having a winning strategy?""",
        r"""Let $ABC$ be an acute triangle with circumcenter $O$ and orthocenter $H$. Let $\Gamma$ denote the circumcircle of triangle $ABC$, and $N$ the midpoint of $OH$. The tangents to $\Gamma$ at $B$ and $C$, and the line through $H$ perpendicular to line $AN$, determine a triangle whose circumcircle we denote by $\omega_A$. Define $\omega_B$ and $\omega_C$ similarly.

        Prove that the common chords of $\omega_A$, $\omega_B$, and $\omega_C$ are concurrent on line $OH$.""",
        r"""A function $f$ from the set of positive real numbers to itself satisfies
        \[f(x+f(y)+xy)=xf(y)+f(x+y)\]
        for all positive real numbers $x$ and $y$. Prove that $f(x)=x$ for all positive real numbers $x$.""",
        r"""The sides of a convex $200$-gon $A_1A_2\ldots A_{200}$ are colored red and blue in an alternating fashion. Suppose the extensions of the red sides determine a regular $100$-gon, as do the extensions of the blue sides.

        Prove that the $50$ diagonals $\overline{A_1A_{101}}$, $\overline{A_3A_{103}}$, $\ldots$, $\overline{A_{99}A_{199}}$ are concurrent.""",
        r"""Prove that for every odd integer $n>1$, there exist integers $a,b>0$ such that, if we let $Q(x)=(x+a)^2+b$, then the following conditions hold:
        \begin{itemize}
        \item we have $\gcd(a,n)=\gcd(b,n)=1$;
        \item the number $Q(0)$ is divisible by $n$; and
        \item the numbers $Q(1)$, $Q(2)$, $Q(3)$, $\ldots$ each have a prime factor not dividing $n$.
        \end{itemize}""",
    ],
    2021: [
        r"""Let $n$ be a fixed positive integer and consider an $n\times n$ grid of real numbers. Determine the greatest possible number of cells $c$ in the grid such that the entry in $c$ is both strictly \emph{greater} than the average of $c$'s column and strictly \emph{less} than the average of $c$'s row.""",
        r"""Find all integers $n\ge 1$ such that $2^n-1$ has exactly $n$ positive integer divisors.""",
        r"""Let $A_1C_2B_1A_2C_1B_2$ be an equilateral hexagon. Let $O_1$ and $H_1$ denote the circumcenter and orthocenter of $\triangle A_1B_1C_1$, and let $O_2$ and $H_2$ denote the circumcenter and orthocenter of $\triangle A_2B_2C_2$. Suppose that $O_1\ne O_2$ and $H_1\ne H_2$. Prove that the lines $O_1O_2$ and $H_1H_2$ are either parallel or coincide.""",
        r"""Let $ABC$ be a triangle with circumcircle $\omega$, and let $X$ be the reflection of $A$ in $B$. Line $CX$ meets $\omega$ again at $D$. Lines $BD$ and $AC$ meet at $E$, and lines $AD$ and $BC$ meet at $F$. Let $M$ and $N$ denote the midpoints of $AB$ and $AC$.

        Can line $EF$ share a point with the circumcircle of triangle $AMN$?""",
        r"""Given a polynomial $p(x)$ with real coefficients, we denote by $S(p)$ the sum of the squares of its coefficients. For example, $S(20x+21)=20^2+21^2=841$.

        Prove that if $f(x)$, $g(x)$, and $h(x)$ are polynomials with real coefficients satisfying the identity $f(x)\cdot g(x)=h(x)^2$, then
        \[S(f)\cdot S(g)\ge S(h)^2.\]""",
        r"""A \emph{bagel} is a loop of $2a+2b+4$ unit squares which can be obtained by cutting a concentric $a\times b$ hole out of an $(a+2)\times(b+2)$ rectangle, for some positive integers $a$ and $b$. (The side of length $a$ of the hole is parallel to the side of length $a+2$ of the rectangle.)

        Consider an infinite grid of unit square cells. For each even integer $n\ge 8$, a \emph{bakery of order $n$} is a finite set of cells $S$ such that, for every $n$-cell bagel $B$ in the grid, there exists a congruent copy of $B$ all of whose cells are in $S$. (The copy can be translated and rotated.) We denote by $f(n)$ the smallest possible number of cells in a bakery of order $n$.

        Find a real number $\alpha$ such that, for all sufficiently large even integers $n\ge 8$, we have
        \[\frac{1}{100}<\frac{f(n)}{n^\alpha}<100.\]""",
    ],
    2022: [
        r"""A \emph{stick} is defined as a $1\times k$ or $k\times 1$ rectangle for any integer $k\ge 1$. We wish to partition the cells of a $2022\times 2022$ chessboard into $m$ non-overlapping sticks, such that any two of these $m$ sticks share at most one unit of perimeter. Determine the smallest $m$ for which this is possible.""",
        r"""A function $\psi\colon\mathbb{Z}\to\mathbb{Z}$ is said to be \emph{zero-requiem} if for any positive integer $n$ and any integers $a_1,\ldots,a_n$ (not necessarily distinct), the sums $a_1+a_2+\cdots+a_n$ and $\psi(a_1)+\psi(a_2)+\cdots+\psi(a_n)$ are not both zero.

        Let $f$ and $g$ be two zero-requiem functions for which $f\circ g$ and $g\circ f$ are both the identity function (that is, $f$ and $g$ are mutually inverse bijections). Given that $f+g$ is \emph{not} a zero-requiem function, prove that $f\circ f$ and $g\circ g$ are both zero-requiem.

        (Recall that if $\psi_1$ and $\psi_2$ are functions from $\mathbb{Z}$ to $\mathbb{Z}$, then the composition $\psi_1\circ\psi_2$ is defined as the function sending each $x\in\mathbb{Z}$ to $\psi_1(\psi_2(x))$, while the sum $\psi_1+\psi_2$ is defined as the function sending each $x\in\mathbb{Z}$ to $\psi_1(x)+\psi_2(x)$.)""",
        r"""Point $P$ lies in the interior of a triangle $ABC$. Lines $AP$, $BP$, and $CP$ meet the opposite sides of triangle $ABC$ at points $A'$, $B'$, and $C'$, respectively. Let $P_A$ be the midpoint of the segment joining the incenters of triangles $BPC'$ and $CPB'$, and define points $P_B$ and $P_C$ analogously. Show that if
        \[AB'+BC'+CA'=AC'+BA'+CB',\]
        then points $P$, $P_A$, $P_B$, and $P_C$ are concyclic.""",
        r"""Let $ABCD$ be a cyclic quadrilateral whose opposite sides are not parallel. Suppose points $P$, $Q$, $R$, $S$ lie in the interiors of segments $AB$, $BC$, $CD$, $DA$, respectively, such that
        \[\angle PDA=\angle PCB,\quad \angle QAB=\angle QDC,\quad \angle RBC=\angle RAD,\quad\text{and}\quad \angle SCD=\angle SBA.\]
        Let $\overline{AQ}$ intersect $\overline{BS}$ at $X$, and $\overline{DQ}$ intersect $\overline{CS}$ at $Y$. Prove that lines $\overline{PR}$ and $\overline{XY}$ are either parallel or coincide.""",
        r"""Let $\tau(n)$ denote the number of positive integer divisors of a positive integer $n$ (for example, $\tau(2022)=8$). Given a polynomial $P(X)$ with integer coefficients, we define a sequence $a_1,a_2,\ldots$ of nonnegative integers by setting
        \[a_n=\begin{cases}\gcd\bigl(P(n),\ \tau(P(n))\bigr) & \text{if } P(n)>0\\ 0 & \text{if } P(n)\le 0\end{cases}\]
        for each positive integer $n$. We then say the sequence \emph{has limit infinity} if every integer occurs in this sequence only finitely many times (possibly not at all).

        Does there exist a choice of $P(X)$ for which the sequence $a_1,a_2,\ldots$ has limit infinity?""",
        r"""Find all positive integers $k$ for which there exists a nonlinear function $f\colon\mathbb{Z}\to\mathbb{Z}$ such that the equation
        \[f(a)+f(b)+f(c)=\frac{f(a-b)+f(b-c)+f(c-a)}{k}\]
        holds for any integers $a$, $b$, $c$ satisfying $a+b+c=0$ (not necessarily distinct).

        (We say $f\colon\mathbb{Z}\to\mathbb{Z}$ is \emph{nonlinear} if $f(x)\ne(f(1)-f(0))x+f(0)$ for some $x\in\mathbb{Z}$.)""",
    ],
    2023: [
        r"""A positive integer $n$ is called \emph{beautiful} if, for every integer $4\le b\le 10000$, the base-$b$ representation of $n$ contains the consecutive digits $2$, $0$, $2$, $3$ (in this order, from left to right). Determine whether the set of all beautiful integers is finite.""",
        r"""Each point in the plane is labeled with a real number. Show that there exist two distinct points $P$ and $Q$ whose labels differ by less than the distance from $P$ to $Q$.""",
        r"""Canmoo is trying to do constructions, but doesn't have a ruler or compass. Instead, Canmoo has a device that, given four distinct points $A$, $B$, $C$, $P$ in the plane, will mark the isogonal conjugate of $P$ with respect to triangle $ABC$, if it exists. Show that if two points are marked on the plane, then Canmoo can construct their midpoint using this device, a pencil for marking additional points, and no other tools.

        (Recall that the isogonal conjugate of $P$ with respect to triangle $ABC$ is the point $Q$ such that lines $AP$ and $AQ$ are reflections around the bisector of $\angle BAC$, lines $BP$ and $BQ$ are reflections around the bisector of $\angle CBA$, lines $CP$ and $CQ$ are reflections around the bisector of $\angle ACB$. Additional points marked by the pencil can be assumed to be in general position, meaning they don't lie on any line through two existing points or any circle through three existing points.)""",
        r"""Let $ABC$ be an acute triangle with orthocenter $H$. Points $A_1$, $B_1$, $C_1$ are chosen in the interiors of sides $BC$, $CA$, $AB$, respectively, such that $\triangle A_1B_1C_1$ has orthocenter $H$. Define $A_2=\overline{AH}\cap\overline{B_1C_1}$, $B_2=\overline{BH}\cap\overline{C_1A_1}$, and $C_2=\overline{CH}\cap\overline{A_1B_1}$.

        Prove that triangle $A_2B_2C_2$ has orthocenter $H$.""",
        r"""Let $n\ge 2$ be an integer. A cube of size $n\times n\times n$ is dissected into $n^3$ unit cubes. A nonzero real number is written at the center of each unit cube so that the sum of the $n^2$ numbers in each slab of size $1\times n\times n$, $n\times 1\times n$, or $n\times n\times 1$ equals zero. (There are a total of $3n$ such slabs, forming three groups of $n$ slabs each such that slabs in the same group are parallel and slabs in different groups are perpendicular.)

        Could it happen that some plane in three-dimensional space separates the positive and the negative written numbers? (The plane should not pass through any of the numbers.)""",
        r"""Let $n\ge 2$ be a fixed integer.
        \begin{enumerate}
        \item[(a)] Determine the largest positive integer $m$ (in terms of $n$) such that there exist complex numbers $r_1,\ldots,r_n$, not all zero, for which
        \[\prod_{k=1}^{n}(r_k+1)=\prod_{k=1}^{n}(r_k^2+1)=\cdots=\prod_{k=1}^{n}(r_k^m+1)=1.\]
        \item[(b)] For this value of $m$, find all possible values of
        \[\prod_{k=1}^{n}(r_k^{m+1}+1).\]
        \end{enumerate}""",
    ],
    2024: [
        r"""There are $1001$ stacks of coins $S_1,S_2,\ldots,S_{1001}$. Initially, stack $S_k$ has $k$ coins for each $k=1,2,\ldots,1001$. In an operation, one selects an ordered pair $(i,j)$ of indices $i$ and $j$ satisfying $1\le i<j\le 1001$ subject to two conditions:
        \begin{itemize}
        \item The stacks $S_i$ and $S_j$ must each have at least one coin.
        \item The ordered pair $(i,j)$ must not have been selected in any previous operation.
        \end{itemize}
        Then, if $S_i$ and $S_j$ have $a$ coins and $b$ coins, respectively, one removes $\gcd(a,b)$ coins from each stack.

        What is the maximum number of times this operation could be performed?""",
        r"""Let $k$ be a fixed positive integer. For each integer $1\le i\le 4$, let $x_i$ and $y_i$ be positive integers such that their least common multiple is $k$. Suppose that the four points $(x_1,y_1)$, $(x_2,y_2)$, $(x_3,y_3)$, $(x_4,y_4)$ are the vertices of a non-degenerate rectangle in the Cartesian plane. Prove that $x_1x_2x_3x_4$ is a perfect square.""",
        r"""Let $ABC$ be an acute triangle with incenter $I$. Two distinct points $P$ and $Q$ are chosen on the circumcircle of $ABC$ such that
        \[\angle API=\angle AQI=45^\circ.\]
        Lines $PQ$ and $BC$ meet at $S$. Let $H$ denote the foot of the altitude from $A$ to $BC$. Prove that $\angle AHI=\angle ISH$.""",
        r"""Find all sequences $a_1,a_2,\ldots$ of nonnegative integers such that for all positive integers $n$, the polynomial
        \[1+x^{a_1}+x^{a_2}+\cdots+x^{a_n}\]
        has at least one integer root. (Here $x^0=1$.)""",
        r"""Let $ABC$ be a scalene triangle whose incircle is tangent to $BC$, $CA$, $AB$ at $D$, $E$, $F$ respectively. Lines $BE$ and $CF$ meet at $G$. Prove that there exists a point $X$ on the circumcircle of triangle $EFG$ such that the circumcircles of triangles $BCX$ and $EFG$ are tangent, and
        \[\angle BGC=\angle BXC+\angle EDF.\]""",
        r"""Let $n$ be an odd positive integer and consider an $n\times n$ chessboard of $n^2$ unit squares. In some of the cells of the chessboard, we place a knight. A knight in a cell $c$ is said to \emph{attack} a cell $c'$ if the distance between the centers of $c$ and $c'$ is exactly $\sqrt5$ (in particular, a knight does not attack the cell which it occupies).

        Suppose each cell of the board is attacked by an even number of knights (possibly zero). Show that the configuration of knights is symmetric with respect to all four axes of symmetry of the board (i.e. the configuration of knights is both horizontally and vertically symmetric, and also unchanged by reflection along either diagonal of the chessboard).""",
    ],
    2025: [
        r"""Find all real numbers $\lambda$ for which there exists an integer $n\ge 2$ and an arithmetic progression $(a_0,a_1,\ldots,a_n)$ of real numbers (in that order) such that the identity
        \[(X-\lambda)(X-\lambda^2)\cdots(X-\lambda^n)=a_0X^n+a_1X^{n-1}+a_2X^{n-2}+\cdots+a_n\]
        is true for every real number $X$.""",
        r"""Let $ABC$ be a fixed triangle with circumcircle $\omega$. Consider $P$ a variable point inside $ABC$. Ray $BP$ meets side $AC$ at $Y$ while ray $CP$ meets side $AB$ at $X$. Let $Q$ be the second intersection of $\omega$ and the circumcircle of triangle $AXY$. Let $K$ be the second intersection of ray $AP$ and $\omega$.

        Prove that as $P$ varies, the circumcircles of triangle $QPK$ all have a common radical center.""",
        # The paper illustrates a move with a picture; it is described in words here.
        r"""Suppose $2025$ black and white mice are arranged in a $45\times 45$ grid. A set of four mice is \emph{special} if the four mice form a contiguous $2\times 2$ square, the top-left mouse and the bottom-right mouse are both black, and the bottom-left mouse and top-right mouse are both white. A \emph{move} swaps the positions of the black and white mice in a special set, so that afterwards its top-left and bottom-right mice are white and its bottom-left and top-right mice are black.

        Across all possible initial configurations of mice, what is the maximum number of moves that one could make?""",
        r"""Determine all odd integers $n\ge 3$ with the following property: Let $S$ denote the set of all positive integers less than $n$ which are relatively prime to $n$, and let $k=\tfrac12|S|$. Then one can label the integers in $S$ by $a_1,\ldots,a_{2k}$ in some order such that
        \[\sum_{i=1}^{k}a_i^2=\frac12\sum_{i=1}^{k}a_ia_{i+k}.\]""",
        r"""Azza and Bob are playing the \emph{squeakuences game}, a game whose rules depend on two positive integers $n$ and $g$ known to both players. A \emph{squeakuence} is an ordered sequence of $100$ integers (not necessarily positive). At the start of the game, Azza gives Bob a list of $n$ different squeakuences, and Bob secretly picks one squeakuence and copies it into a notebook which Azza cannot see.

        On each turn of the game, Azza makes up to $g$ guesses for the squeakuence currently in the notebook. Bob hears all of Azza's guesses. If any of Azza's guesses are correct, the game ends and Azza wins. Otherwise, Bob privately chooses an index $1\le i\le 100$ and an integer $\delta\in\{-1,0,1\}$, and secretly modifies the squeakuence written in the notebook by adding $\delta$ to its $i$th entry. (Azza is not told either $i$ or $\delta$. The values of $i$ and $\delta$ can change from turn to turn.)

        Find the smallest real number $\alpha$ for which there exists $C>0$ making the following statement true: Azza can always guarantee winning the squeakuences game provided that $g>Cn^\alpha$.""",
        r"""Let $k$ be a positive integer not divisible by $6$. Suppose that there exists a prime $p$ such that $p$ divides both $2025^k-1$ and $2026^k-1$. Prove that $p<3^k$.""",
    ],
}


def compact(value: str) -> str:
    """Dedent editorial text, keeping paragraph breaks and display/list lines."""
    value = textwrap.dedent(value).strip()
    paragraphs = re.split(r"\n\s*\n", value)
    return "\n\n".join(
        "\n".join(line.strip() for line in p.splitlines() if line.strip())
        for p in paragraphs
    )


def build_records() -> list[dict]:
    records = []
    for year in sorted(STATEMENTS):
        statements = STATEMENTS[year]
        if len(statements) != 6 or len(TOPICS[year]) != 6:
            raise ValueError(f"expected six problems for USEMO {year}")
        for number, (topic, body) in enumerate(zip(TOPICS[year], statements), start=1):
            records.append({
                "id": f"USEMO-{year}-{number}",
                "source": "USEMO",
                "year": year,
                "code": f"{topic}{number}",
                "subject": SUBJECTS[topic],
                "level": LEVELS[number],
                "country": "",
                "format": "latex",
                "body": compact(body),
                "url": paper_url(year),
            })
    return records


def write_bank(path: Path, records: list[dict]) -> None:
    lines = [
        "/* US Ersatz Math Olympiad, 2019-2025 (7 papers, 42 problems).",
        "   Statements transcribed from the official papers at web.evanchen.cc/usemo.html. */",
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
    parser.add_argument("--output", type=Path, default=Path("bank_usemo.js"))
    args = parser.parse_args()

    records = build_records()
    if len(records) != 42 or len({record["id"] for record in records}) != 42:
        raise ValueError("USEMO bank must contain exactly 42 unique records")
    write_bank(args.output, records)
    print(f"wrote {len(records)} problems to {args.output}")


if __name__ == "__main__":
    main()
