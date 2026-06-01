# IMO Shortlist 2021 problems
_fidelity: approx (math glyphs recovered best-effort)_

## A1 — Algebra

```
Let n be an integer, and let A be a subset of t0, 1, 2, 3, . . . , 5 u consisting of 4n + 2         n

numbers. Prove that there exist a, b, c P A such that a < b < c and c + 2a > 3b.
```

## A2 — Algebra

```
For every integer n ≥ 1 consider the n ˆ n table with entry n + 1 at the intersection
                                                                                                    Z        ^
                                                                                                        ij

of row i and column j , for every i = 1, . . . , n and j = 1, . . . , n. Determine all integers n ≥ 1 for
which the sum of the n2 entries in the table is equal to 14 n2pn − 1q.
```

## A3 — Algebra

```
Given a positive integer n, find the smallest value of Y a1 ] + Y a2 ] + ··· + Y an ] over1            2   n

all permutations pa1 , a2, . . . , an q of p1, 2, . . . , nq.
```

## A4 — Algebra

```
Show that for all real numbers x , . . . , x the following inequality holds:
                                                     1               n

                                     ÿ n b
                                     n ÿ                             ÿ n b
                                               |xi − xj | ≤                     |xi + xj |.
                                    i 1j 1                           = =
```

## A5 — Algebra

```
Let n ≥ 2 be an integer, and let a , a , . . . , a be positive real numbers such that
                                                             1       2          n
a1 + a2 + ··· + an = 1. Prove that
                                           ak
                                                pa1 + a2 + ··· + ak−1 q2 < .
                                    k =1
```

## A6 — Algebra

```
Let A be a finite set of (not necessarily positive) integers, and let m ≥ 2 be an integer.
Assume that there exist non-empty subsets B1 , B2, B3, . . . , Bm of A whose elements add up to
the sums m1 , m2 , m3, . . . , mm, respectively. Prove that A contains at least m{2 elements.
```

## A7 — Algebra

```
Let n ≥ 1 be an integer, and let x , x , . . . , x + be n + 2 non-negative real numbers
                                                         0       1            n 1
that satisfy xi xi+1 − x2i−1 ≥ 1 for all i = 1, 2, . . . , n. Show that
                                                                               ˆ         ˙3{2
                                    x0 + x1 + ··· + xn + xn+1 >
```

## A8 — Algebra

```
Determine all functions f : R → R that satisfy
       +               ˘+                ˘+                  ˘
        f paq − f pbq       f pbq − f pcq   f pcq − f paq        = f pab2 + bc2 + ca2 q − f pa2b + b2 c + c2aq
for all real numbers a, b, c.

6                                               Saint-Petersburg — Russia, 16th–24th July 2021
```

## C1 — Combinatorics

```
Let S be an infinite set of positive integers, such that there exist four pairwise distinct
a, b, c, d P S with gcdpa, bq ‰ gcdpc, dq. Prove that there exist three pairwise distinct x, y, z P S
such that gcdpx, y q = gcdpy, zq ‰ gcdpz, xq.
```

## C2 — Combinatorics

```
Let n ≥ 3 be an integer. An integer m ≥ n + 1 is called n-colourful if, given infinitely
many marbles in each of n colours C1, C2, . . . , Cn , it is possible to place m of them around a
circle so that in any group of n + 1 consecutive marbles there is at least one marble of colour
Ci for each i = 1, . . . , n.
    Prove that there are only finitely many positive integers which are not n-colourful. Find
the largest among them.
```

## C3 — Combinatorics

```
A thimblerigger has 2021 thimbles numbered from 1 through 2021. The thimbles are
arranged in a circle in arbitrary order. The thimblerigger performs a sequence of 2021 moves;
in the kth move, he swaps the positions of the two thimbles adjacent to thimble k.
    Prove that there exists a value of k such that, in the kth move, the thimblerigger swaps
some thimbles a and b such that a < k < b.
```

## C4 — Combinatorics

```
The kingdom of Anisotropy consists of n cities. For every two cities there exists exactly
one direct one-way road between them. We say that a path from X to Y is a sequence of roads
such that one can move from X to Y along this sequence without returning to an already
visited city. A collection of paths is called diverse if no road belongs to two or more paths in
the collection.
    Let A and B be two distinct cities in Anisotropy. Let NAB denote the maximal number of
paths in a diverse collection of paths from A to B . Similarly, let NBA denote the maximal num-
ber of paths in a diverse collection of paths from B to A. Prove that the equality NAB = NBA
holds if and only if the number of roads going out from A is the same as the number of roads
going out from B .
```

## C5 — Combinatorics

```
Let n and k be two integers with n > k ≥ 1. There are 2n + 1 students standing in
a circle. Each student S has 2k neighbours — namely, the k students closest to S on the right,
and the k students closest to S on the left.
    Suppose that n + 1 of the students are girls, and the other n are boys. Prove that there is
a girl with at least k girls among her neighbours.
```

## C6 — Combinatorics

```
A hunter and an invisible rabbit play a game on an infinite square grid. First the
hunter fixes a colouring of the cells with finitely many colours. The rabbit then secretly chooses
a cell to start in. Every minute, the rabbit reports the colour of its current cell to the hunter,
and then secretly moves to an adjacent cell that it has not visited before (two cells are adjacent
if they share a side). The hunter wins if after some finite time either
    • the rabbit cannot move; or

    • the hunter can determine the cell in which the rabbit started.

Decide whether there exists a winning strategy for the hunter.

Shortlisted problems                                                                                7
```

## C7 — Combinatorics

```
Consider a checkered 3m ˆ 3m square, where m is an integer greater than 1. A frog
sits on the lower left corner cell S and wants to get to the upper right corner cell F . The frog
can hop from any cell to either the next cell to the right or the next cell upwards.
    Some cells can be sticky, and the frog gets trapped once it hops on such a cell. A set X of
cells is called blocking if the frog cannot reach F from S when all the cells of X are sticky. A
blocking set is minimal if it does not contain a smaller blocking set.
(a) Prove that there exists a minimal blocking set containing at least 3m2 − 3m cells.
(b) Prove that every minimal blocking set contains at most 3m2 cells.
Note. An example of a minimal blocking set for m = 2 is shown below. Cells of the set X are marked
by letters x.
                                        S      x
```

## C8 — Combinatorics

```
Determine the largest N for which there exists a table T of integers with N rows and
100 columns that has the following properties:

  (i) Every row contains the numbers 1, 2, . . . , 100 in some order.
 (ii) For any two distinct rows r and s, there is a column c such that |T pr, cq − T ps, cq| ≥ 2.
    Here T pr, cq means the number at the intersection of the row r and the column c.

8                                              Saint-Petersburg — Russia, 16th–24th July 2021
```

## G1 — Geometry

```
Let ABCD be a parallelogram such that AC = BC . A point P is chosen on the
extension of the segment AB beyond B . The circumcircle of the triangle ACD meets the
segment P D again at Q, and the circumcircle of the triangle AP Q meets the segment P C
again at R. Prove that the lines CD, AQ, and BR are concurrent.
```

## G2 — Geometry

```
Let ABCD be a convex quadrilateral circumscribed around a circle with centre I .
Let ω be the circumcircle of the triangle ACI . The extensions of BA and BC beyond A and
C meet ω at X and Z , respectively. The extensions of AD and CD beyond D meet ω at Y
and T , respectively. Prove that the perimeters of the (possibly self-intersecting) quadrilaterals
ADT X and CDY Z are equal.
```

## G3 — Geometry

```
Version 1. Let n be a fixed positive integer, and let S be the set of points px, y q on the
Cartesian plane such that both coordinates x and y are nonnegative integers smaller than 2n
(thus |S| = 4n2 ). Assume that F is a set consisting of n2 quadrilaterals such that all their
vertices lie in S, and each point in S is a vertex of exactly one of the quadrilaterals in F .
    Determine the largest possible sum of areas of all n2 quadrilaterals in F .
Version 2. Let n be a fixed positive integer, and let S be the set of points px, y q on the
Cartesian plane such that both coordinates x and y are nonnegative integers smaller than 2n
(thus |S| = 4n2). Assume that F is a set of polygons such that all vertices of polygons in F lie
in S, and each point in S is a vertex of exactly one of the polygons in F .
    Determine the largest possible sum of areas of all polygons in F .
```

## G4 — Geometry

```
Let ABCD be a quadrilateral inscribed in a circle Ω. Let the tangent to Ω at D
intersect the rays BA and BC at points E and F , respectively. A point T is chosen inside the
triangle ABC so that T E k CD and T F k AD. Let K ‰ D be a point on the segment DF
such that T D = T K . Prove that the lines AC , DT and BK intersect at one point.
```

## G5 — Geometry

```
Let ABCD be a cyclic quadrilateral whose sides have pairwise different lengths. Let
O be the circumcentre of ABCD . The internal angle bisectors of =ABC and =ADC meet AC
at B1 and D1, respectively. Let OB be the centre of the circle which passes through B and is
tangent to AC at D1. Similarly, let OD be the centre of the circle which passes through D and
is tangent to AC at B1 .
    Assume that BD1 k DB1. Prove that O lies on the line OB OD .
```

## G6 — Geometry  (Every polygon is assumed to contain its boundary.)

```
Determine all integers n ≥ 3 satisfying the following property: every convex n-gon
whose sides all have length 1 contains an equilateral triangle of side length 1.
  (Every polygon is assumed to contain its boundary.)

Shortlisted problems                                                                          9
```

## G7 — Geometry

```
A point D is chosen inside an acute-angled triangle ABC with AB > AC so that
=BAD = =DAC . A point E is constructed on the segment AC so that =ADE = =DCB .
Similarly, a point F is constructed on the segment AB so that =ADF = =DBC . A point
X is chosen on the line AC so that CX = BX . Let O1 and O2 be the circumcentres of the
triangles ADC and DXE . Prove that the lines BC , EF , and O1O2 are concurrent.
```

## G8 — Geometry

```
Let ω be the circumcircle of a triangle ABC , and let Ω be its excircle which is tangent
to the segment BC . Let X and Y be the intersection points of ω and ΩA . Let P and Q be the
projections of A onto the tangent lines to ΩA at X and Y , respectively. The tangent line at P
to the circumcircle of the triangle AP X intersects the tangent line at Q to the circumcircle of
the triangle AQY at a point R. Prove that AR K BC .

10                                                   Saint-Petersburg — Russia, 16th–24th July 2021
```

## N1 — Number Theory

```
Determine all integers n ≥ 1 for which there exists a pair of positive integers pa, bq
such that no cube of a prime divides a2 + b + 3 and
                                               ab + 3b + 8
                                               a2 + b + 3
                                                           = n.
```

## N2 — Number Theory

```
Let n ≥ 100 be an integer. The numbers n, n + 1, . . . , 2n are written on n + 1 cards,
one number per card. The cards are shuffled and divided into two piles. Prove that one of the
piles contains two cards such that the sum of their numbers is a perfect square.
```

## N3 — Number Theory

```
Find all positive integers n with the following property: the k positive divisors of n
have a permutation pd1, d2, . . . , dk q such that for every i = 1, 2, . . . , k, the number d1 + ··· + di
is a perfect square.
```

## N4 — Number Theory

```
Alice is given a rational number r > 1 and a line with two points B ‰ R, where
point R contains a red bead and point B contains a blue bead. Alice plays a solitaire game by
performing a sequence of moves. In every move, she chooses a (not necessarily positive) integer
k , and a bead to move. If that bead is placed at point X , and the other bead is placed at Y ,
                                                     ÝÝ→
then Alice moves the chosen bead to point X 1 with Y X 1 = rk Ý Ý→
                                                               Y X.
     Alice’s goal is to move the red bead to the point B . Find all rational numbers r > 1 such
that Alice can reach her goal in at most 2021 moves.
```

## N5 — Number Theory

```
Prove that there are only finitely many quadruples pa, b, c, nq of positive integers such
that
                                         n! = an−1 + bn−1 + cn−1 .
```

## N6 — Number Theory

```
Determine all integers n ≥ 2 with the following property: every n pairwise distinct
integers whose sum is not divisible by n can be arranged in some order a1 , a2 , . . . , an so that
n divides 1 · a1 + 2 · a2 + ··· + n · an .
```

## N7 — Number Theory

```
Let a , a , a , . . . be an infinite sequence of positive integers such that a + divides
                 1   2   3                                                                   n 2m
an + an+m for all positive integers n and m. Prove that this sequence is eventually periodic, i.e.
there exist positive integers N and d such that an = an+d for all n > N .
```

## N8 — Number Theory

```
For a polynomial P pxq with integer coefficients let P 1pxq = P pxq and P k+1pxq =
P pP k pxqq for k ≥ 1. Find all positive integers n for which there exists a polynomial P pxq with
integer coefficients such that for every integer m ≥ 1, the numbers P mp1q, . . . , P mpnq leave
exactly rn{2m s distinct remainders when divided by n.

Shortlisted problems – solutions                                       11

12   Saint-Petersburg — Russia, 16th–24th July 2021

Shortlisted problems – solutions                                                                 13

                                       Solutions
A1. Let n be an integer, and let A be a subset of t0, 1, 2, 3, . . . , 5 u consisting of 4n + 2

numbers. Prove that there exist a, b, c P A such that a < b < c and c + 2a > 3b.
```
