#!/usr/bin/env python3
"""Write the 31 ISL-2024 problems as clean LaTeX, transcribed from rendered pages."""
from pathlib import Path

P = {
("A1","Colombia"): r"""Determine all real numbers $\alpha$ such that the number
\[ \lfloor \alpha \rfloor + \lfloor 2\alpha \rfloor + \cdots + \lfloor n\alpha \rfloor \]
is a multiple of $n$ for every positive integer $n$. (Here $\lfloor z \rfloor$ denotes the greatest integer less than or equal to $z$.)""",

("A2","China"): r"""Let $n$ be a positive integer. Find the minimum possible value of
\[ S = 2^0 x_0^2 + 2^1 x_1^2 + \cdots + 2^n x_n^2, \]
where $x_0, x_1, \ldots, x_n$ are nonnegative integers such that $x_0 + x_1 + \cdots + x_n = n$.""",

("A3","China"): r"""Decide whether for every sequence $(a_n)$ of positive real numbers,
\[ \frac{3^{a_1} + 3^{a_2} + \cdots + 3^{a_n}}{\left(2^{a_1} + 2^{a_2} + \cdots + 2^{a_n}\right)^2} < \frac{1}{2024} \]
is true for at least one positive integer $n$.""",

("A4","Thailand"): r"""Let $\mathbb{Z}_{>0}$ be the set of all positive integers. Determine all subsets $\mathcal{S}$ of $\{2^0, 2^1, 2^2, \ldots\}$ for which there exists a function $f : \mathbb{Z}_{>0} \to \mathbb{Z}_{>0}$ such that
\[ \mathcal{S} = \{ f(a+b) - f(a) - f(b) \mid a, b \in \mathbb{Z}_{>0} \}. \]""",

("A5","Kosovo"): r"""Find all periodic sequences $a_1, a_2, \ldots$ of real numbers such that the following conditions hold for all $n \geq 1$:
\[ a_{n+2} + a_n^2 = a_n + a_{n+1}^2 \qquad \text{and} \qquad |a_{n+1} - a_n| \leq 1. \]""",

("A6","Czech Republic"): r"""Let $a_0, a_1, a_2, \ldots$ be an infinite strictly increasing sequence of positive integers such that for each $n \geq 1$ we have
\[ a_n \in \left\{ \frac{a_{n-1} + a_{n+1}}{2},\ \sqrt{a_{n-1} \cdot a_{n+1}} \right\}. \]
Let $b_1, b_2, \ldots$ be an infinite sequence of letters defined as
\[ b_n = \begin{cases} A, & \text{if } a_n = \tfrac{1}{2}(a_{n-1} + a_{n+1}); \\ G, & \text{otherwise.} \end{cases} \]
Prove that there exist positive integers $n_0$ and $d$ such that for all $n \geq n_0$ we have $b_{n+d} = b_n$.""",

("A7","Japan"): r"""Let $\mathbb{Q}$ be the set of rational numbers. Let $f : \mathbb{Q} \to \mathbb{Q}$ be a function such that the following property holds: for all $x, y \in \mathbb{Q}$,
\[ f(x + f(y)) = f(x) + y \qquad \text{or} \qquad f(f(x) + y) = x + f(y). \]
Determine the maximum possible number of elements of $\{ f(x) + f(-x) \mid x \in \mathbb{Q} \}$.""",

("A8","Japan"): r"""Let $p \neq q$ be coprime positive integers. Determine all infinite sequences $a_1, a_2, \ldots$ of positive integers such that the following conditions hold for all $n \geq 1$:
\begin{align*}
\max(a_n, a_{n+1}, \ldots, a_{n+p}) - \min(a_n, a_{n+1}, \ldots, a_{n+p}) &= p \qquad \text{and} \\
\max(a_n, a_{n+1}, \ldots, a_{n+q}) - \min(a_n, a_{n+1}, \ldots, a_{n+q}) &= q.
\end{align*}""",

("C1","Australia"): r"""Let $n$ be a positive integer. A class of $n$ students run $n$ races, in each of which they are ranked with no draws. A student is eligible for a rating $(a, b)$ for positive integers $a$ and $b$ if they come in the top $b$ places in at least $a$ of the races. Their final score is the maximum possible value of $a - b$ across all ratings for which they are eligible. Find the maximum possible sum of all the scores of the $n$ students.""",

("C2","Türkiye"): r"""Let $n$ be a positive integer. The integers $1, 2, 3, \ldots, n^2$ are to be written in the cells of an $n \times n$ board such that each integer is written in exactly one cell and each cell contains exactly one integer. For every integer $d$ with $d \mid n$, the $d$-division of the board is the division of the board into $(n/d)^2$ nonoverlapping sub-boards, each of size $d \times d$, such that each cell is contained in exactly one $d \times d$ sub-board.

We say that $n$ is a \emph{cool} number if the integers can be written on the $n \times n$ board such that, for each integer $d$ with $d \mid n$ and $1 < d < n$, in the $d$-division of the board, the sum of the integers written in each $d \times d$ sub-board is not a multiple of $d$. Determine all even cool numbers.""",

("C3","Belarus"): r"""Let $n$ be a positive integer. There are $2n$ knights sitting at a round table. They consist of $n$ pairs of partners, each pair of which wishes to shake hands. A pair can shake hands only when next to each other. Every minute, one pair of adjacent knights swaps places.

Find the minimum number of exchanges of adjacent knights such that, regardless of the initial arrangement, every knight can shake hands with their partner at some point in time.""",

("C4","Hong Kong"): r"""On a board with $2024$ rows and $2023$ columns, Turbo the snail sits in a cell. He wants to move from the first row to the last row. On each attempt he chooses to start on a cell in the first row, then he repeatedly moves to an adjacent cell sharing a common side; he wins if he reaches any cell in the last row.

However, there are $2022$ predetermined hidden monsters, one in each row except the first and last, and no two monsters are in the same column. If Turbo reaches a cell with a monster, his attempt ends and he is transported back to start a new attempt. The monsters do not move, and Turbo remembers whether or not each cell he has visited contains a monster.

Determine the minimum value of $n$ for which Turbo has a strategy that guarantees reaching the last row in at most $n$ attempts, regardless of the locations of the monsters.""",

("C5","Indonesia"): r"""Let $N$ be a positive integer. Geoff and Ceri play a game in which they start by writing the numbers $1, 2, \ldots, N$ on a board. They then take turns to make a move, with Geoff going first. Each move consists of choosing a pair of integers $(k, n)$, where $k \geq 0$ is an integer and $n$ is one of the integers on the board, and then erasing every integer $s$ on the board such that $2^k \mid n - s$. The game continues until the board is empty, and the player who erases the last integer loses. Determine all values of $N$ for which Geoff can ensure that he wins, no matter how Ceri plays.""",

("C6","Ghana"): r"""Let $n$ and $T$ be positive integers. James has $4n$ marbles with weights $1, 2, \ldots, 4n$. He places them on the two sides of a balance scale so that both sides have equal weight. Andrew may move a marble from one side of the scale to the other, so long as after the move the absolute difference between the weights of the two sides is at most $T$.

Find, in terms of $n$, the minimum positive integer $T$ such that Andrew can always make a sequence of moves resulting in all of the marbles being on the side they did not start on, regardless of how James initially placed the marbles.""",

("C7","Australia"): r"""Let $N$ be a positive integer. Suppose that, for each $n > N$, the term $a_n$ is equal to the number of times $a_{n-1}$ appears in the list $a_1, a_2, \ldots, a_{n-1}$. Prove that at least one of the sequences $a_1, a_3, a_5, \ldots$ and $a_2, a_4, a_6, \ldots$ is eventually periodic.""",

("C8","Peru"): r"""Let $n$ be a positive integer. Given an $n \times n$ board, the unit cell in the top left corner is initially coloured black, and the other cells are coloured white. We then apply a series of colouring operations to the board. In each operation we choose a $2 \times 2$ square with exactly one black cell, and we colour the remaining three cells of that $2 \times 2$ square black. Determine all values of $n$ such that we can colour the whole board black.""",

("G1","Ukraine"): r"""Let $ABCD$ be a cyclic quadrilateral such that $AC < BD < AD$ and $\angle DBA < 90^\circ$. Point $E$ lies on the line through $D$ parallel to $AB$ such that $E$ and $C$ lie on opposite sides of line $AD$, and $AC = DE$. Point $F$ lies on the line through $A$ parallel to $CD$ such that $F$ and $C$ lie on opposite sides of line $AD$, and $BD = AF$. Prove that the perpendicular bisectors of segments $BC$ and $EF$ intersect on the circumcircle of $ABCD$.""",

("G2","Poland"): r"""Let $ABC$ be a triangle with $AB < AC < BC$, incentre $I$ and incircle $\omega$. Let $X$ be the point on line $BC$ different from $C$ such that the line through $X$ parallel to $AC$ is tangent to $\omega$. Similarly, let $Y$ be the point on line $BC$ different from $B$ such that the line through $Y$ parallel to $AB$ is tangent to $\omega$. Let $AI$ intersect the circumcircle of triangle $ABC$ again at $P \neq A$. Let $K$ and $L$ be the midpoints of $AB$ and $AC$, respectively. Prove that $\angle KIL + \angle YPX = 180^\circ$.""",

("G3","Belarus"): r"""Let $ABCDE$ be a convex pentagon and let $M$ be the midpoint of $AB$. Suppose that segment $AB$ is tangent to the circumcircle of triangle $CME$ at $M$ and that $D$ lies on the circumcircles of triangles $AME$ and $BMC$. Lines $AD$ and $ME$ intersect at $K$, and lines $BD$ and $MC$ intersect at $L$. Points $P$ and $Q$ lie on line $EC$ so that $\angle PDC = \angle EDQ = \angle ADB$. Prove that lines $KP$, $LQ$, and $MD$ are concurrent.""",

("G4","Ukraine"): r"""Let $ABCD$ be a quadrilateral with $AB$ parallel to $CD$ and $AB < CD$. Lines $AD$ and $BC$ intersect at a point $P$. Point $X \neq C$ on the circumcircle of triangle $ABC$ is such that $PC = PX$. Point $Y \neq D$ on the circumcircle of triangle $ABD$ is such that $PD = PY$. Lines $AX$ and $BY$ intersect at $Q$. Prove that $PQ$ is parallel to $AB$.""",

("G5","Uzbekistan"): r"""Let $ABC$ be a triangle with incentre $I$, and let $\Omega$ be the circumcircle of triangle $BIC$. Let $K$ be a point in the interior of segment $BC$ such that $\angle BAK < \angle KAC$. The angle bisector of $\angle AKB$ intersects $\Omega$ at points $W$ and $X$ such that $A$ and $W$ lie on the same side of $BC$, and the angle bisector of $\angle CKA$ intersects $\Omega$ at points $Y$ and $Z$ such that $A$ and $Y$ lie on the same side of $BC$. Prove that $\angle WAY = \angle ZAX$.""",

("G6","Poland"): r"""Let $ABC$ be an acute triangle with $AB < AC$, and let $\Gamma$ be the circumcircle of $ABC$. Points $X$ and $Y$ lie on $\Gamma$ such that $XY$ and $BC$ intersect on the external angle bisector of $\angle BAC$. Suppose that the tangents to $\Gamma$ at $X$ and $Y$ intersect at $T$ on the same side of line $BC$ as $A$, and that $TX$ and $TY$ intersect $BC$ at $U$ and $V$, respectively. Prove that $AJ$ bisects $\angle BAC$, where $J$ is the midpoint of the arc $TUV$.""",

("G7","Thailand"): r"""Let $ABC$ be a triangle with incentre $I$ such that $AB < AC < BC$. The second intersections of $AI$, $BI$, and $CI$ with the circumcircle of triangle $ABC$ are $M_A$, $M_B$, $M_C$, respectively. Lines $AI$ and $BC$ intersect at $D$ and lines $BM_C$ and $CM_B$ intersect at $X$. Suppose the circumcircles of triangles $XM_BM_C$ and $XBC$ intersect again at $P \neq X$ and the circumcircle of triangle $SXM_A$ again at $P \neq X$, respectively. Prove that the circumcentre of triangle $SID$ lies on $PQ$.""",

("G8","Canada"): r"""Let $ABC$ be a triangle with $AB < AC < BC$, and let $D$ be a point in the interior of segment $BC$. Let $E$ be a point on the circumcircle of triangle $ABC$ such that $A$ and $E$ lie on opposite sides of line $BC$ and $\angle BAD = \angle EAC$. Let $I$, $I_B$, $I_C$, $J_B$, and $J_C$ be the incentres of triangles $ABC$, $ABD$, $ADC$, $ABE$, and $AEC$, respectively. Prove that $I_B$, $I_C$, $J_B$, and $J_C$ are concyclic if and only if $AI$, $I_BJ_C$, and $J_BI_C$ concur.""",

("N1","Ghana"): r"""Find all positive integers $n$ with the following property: for all positive divisors $d$ of $n$, we have that $d + 1 \mid n$ or $d + 1$ is prime.""",

("N2","Netherlands"): r"""Determine all finite, nonempty sets $\mathcal{S}$ of positive integers such that for every $a, b \in \mathcal{S}$ there exists $c \in \mathcal{S}$ with $a \mid b + 2c$.""",

("N3","Singapore"): r"""Determine all sequences $a_1, a_2, \ldots$ of positive integers such that, for any pair of positive integers $m \leq n$, the arithmetic and geometric means
\[ \frac{a_m + a_{m+1} + \cdots + a_n}{n - m + 1} \qquad \text{and} \qquad \left(a_m a_{m+1} \cdots a_n\right)^{\frac{1}{n-m+1}} \]
are both integers.""",

("N4","Indonesia"): r"""Determine all positive integers $a$ and $b$ such that there exists a positive integer $g$ such that $\gcd(a^n + b,\ b^n + a) = g$ holds for all sufficiently large $n$.""",

("N5","Croatia"): r"""Let $\mathcal{S}$ be a finite nonempty set of prime numbers. Let $1 = b_1 < b_2 < \cdots$ be the sequence of all positive integers whose prime divisors all belong to $\mathcal{S}$. Prove that, for all but finitely many positive integers $n$, there exist positive integers $a_1, a_2, \ldots, a_n$ such that
\[ \frac{a_1}{b_1} + \frac{a_2}{b_2} + \cdots + \frac{a_n}{b_n} = \left\lceil \frac{1}{b_1} + \frac{1}{b_2} + \cdots + \frac{1}{b_n} \right\rceil. \]""",

("N6","France"): r"""Let $n$ be a positive integer. We say that a polynomial $P$ with integer coefficients is $n$-good if there exists a polynomial $Q$ of degree $2$ with integer coefficients such that $Q(k)P(k) + Q(k))$ is never divisible by $n$ for any integer $k$. Determine all positive integers $n$ such that every polynomial with integer coefficients is an $n$-good polynomial.""",

("N7","Japan"): r"""Let $\mathbb{Z}_{>0}$ denote the set of positive integers. Let $f : \mathbb{Z}_{>0} \to \mathbb{Z}_{>0}$ be a function satisfying the following property: for all $m, n \in \mathbb{Z}_{>0}$, the equation
\[ f(mn)^2 = f(m^2) f(f(n)) f(mf(n)) \]
holds and only if $m$ and $n$ are coprime. For each positive integer $n$, determine all the possible values of $f(n)$.""",
}

out = Path("ISL_problems/2024")
out.mkdir(parents=True, exist_ok=True)
md = ["# IMO Shortlist 2024 — problems (clean LaTeX, vision-transcribed)\n"]
order = {"A":0,"C":1,"G":2,"N":3}
for (code, country), body in sorted(P.items(), key=lambda kv: (order[kv[0][0][0]], int(kv[0][0][1:]))):
    (out / f"{code}.tex").write_text(body.strip() + "\n")
    md.append(f"## {code}  ({country})\n\n{body.strip()}\n")
(out / "_problems_latex.md").write_text("\n".join(md))
print(f"wrote {len(P)} LaTeX problems to {out}/")
