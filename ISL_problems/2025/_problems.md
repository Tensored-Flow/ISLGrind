# IMO Shortlist 2025 problems
_fidelity: approx (math glyphs recovered best-effort)_

## A1 — Algebra

```
Quadratic solitaire is a single-player game. To start the game, the player chooses two
distinct nonzero integers a and b and writes the equation x2 + ax + b = 0 on a blackboard. On
each turn, if the equation currently written on the blackboard has two distinct nonzero integer
solutions x = u and x = v, then the player erases the equation and replaces it by one of the
equations x2 + ux + v = 0 or x2 + vx + u = 0 of their choosing. Otherwise, the game ends.
Determine all initial choices of a and b such that quadratic solitaire can be played forever.
```

## A2 — Algebra

```
The sunshine cost of a sequence a1 , a2 , . . . , a100 of integers is the largest possible value
of
                                      |pa1 + a2 + ··· + ai q − aj |
as i and j vary over all integers 1, 2, . . . , 100.
Determine the smallest possible sunshine cost over all sequences a1 , a2 , . . . , a100 of pairwise
distinct integers.
```

## A3 — Algebra  (Italy)

```
Coral and Joey are playing the inekoalaty game, a two-player game whose rules depend
on a positive real number λ which is known to both players. On the nth turn of the game, the
following happens:

     • If n is odd, Coral chooses a nonnegative real number xn such that

                                          x1 + x2 + ··· + xn ≤ λn.

     • If n is even, Joey chooses a nonnegative real number xn such that

                                          x21 + x22 + ··· + x2n ≤ n.

All chosen numbers are known to both players. If a player cannot make a move, the game ends
and the other player wins.
Determine all values of λ for which Coral has a winning strategy and all those for which Joey
has a winning strategy.
                                                                                       (Italy)
```

## A4 — Algebra

```
Let Z≥0 be the set of all nonnegative integers. Let f : Z≥0 → Z≥0 be an unbounded
function such that, if m and n are nonnegative integers satisfying
                                          ␣                             (
                         f pm + nq = max f p0q, f p1q, . . . , f pm + nq ,

then
                                      f pm + nq = f pmq + f pnq.
Prove that there exist positive integers A, B, C and D such that for all nonnegative integers n,
f pAn + Bq = Cn + D.

We say that f is unbounded if for each nonnegative integer N , there exists some nonnegative
integer n such that f pnq ≥ N .

Shortlisted problems                                                                                     3
```

## A5 — Algebra

```
Determine all integers n ≥ 2 such that the polynomial

                       P px, y, zq = xn + y n + z n − xn−2 yz − xy n−2 z − xyz n−2

can be written as P px, y, zq = Qpx, y, zqRpx, y, zq, where Qpx, y, zq and Rpx, y, zq are noncon-
stant polynomials with integer coefficients.
```

## A6 — Algebra

```
Let S be a set of positive integers, possibly infinite, such that no positive integer greater
than 1 divides all elements of S. Determine all non-periodic infinite sequences a1 , a2 , a3 , . . . of
positive integers such that, for all positive integers n,

   • an ≤ |an+ℓ − ℓ| for all ℓ in S, and

   • an = |an+ℓ − ℓ| for at least one ℓ in S.

We say that an infinite sequence a1 , a2 , a3 , . . . is periodic if there exists a positive integer t such
that an = an+t for all positive integers n.
```

## A7 — Algebra

```
For each integer k ≥ 3, prove that there exists a unique tuple px1 , x2 , . . . , xk q of
positive real numbers such that x1 ≥ x2 ≥ ··· ≥ xk and
                        Z         ^ Z           ^          Z        ^
                                1             1                   1
                          nx1 +    + nx2 +        + ··· + nxk +     =n
                                2             2                   2

for every integer n.

Here tzu denotes the greatest integer less than or equal to z. For example, t−πu = −4 and
t2u = t2.9u = 2.
```

## A8 — Algebra  (France)

```
Tim and Tam play a game. To start the game, Tim writes some nonzero real numbers,
not necessarily distinct, on a blackboard. In each round, the following happens:

   • First, Tam chooses a polynomial Pk pxq = ak xk +ak−1 xk−1 +···+a1 x+a0 whose coefficients
     ak , ak−1 , . . . , a1 , a0 are all of the numbers currently written on the blackboard in some
     order. (For example, if the numbers on the blackboard are 4, −3, 4, then k = 2 and Tam
     may choose the polynomial 4x2 − 3x + 4 or −3x2 + 4x + 4 but not 4x − 3 or −3x2 − 3x + 4.)

   • Then, if the equation Pk pxq = 0 has no real solutions, the game is stopped. Otherwise,
     Tim chooses a real number r such that Pk prq = 0 and writes it on the blackboard, so
     there is now one more number on the blackboard.

Determine whether Tim can ensure that the game is never stopped, no matter what Tam does.
                                                                                 (France)

4                                            Sunshine Coast QLD, Australia, 10th –20th July 2025
```

## C1 — Combinatorics

```
Let n ≥ 3 be an integer, and let Sn be the set of points px, yq in the plane such that
x and y are nonnegative integers and x + y < n. A line in the plane is called interesting if it is
not parallel to the x-axis, the y-axis, or the line x + y = 0.
Determine all nonnegative integers k such that there exist n lines satisfying both of the following:

     • the union of the n lines contains every point of Sn , and

     • exactly k of the lines are interesting.
```

## C2 — Combinatorics

```
There is a row of n paddocks, labelled from left to right with the integers 1 to n,
where n ≥ 3. Skippy the Kangaroo grazes in the paddocks according to the following rule:

       If Skippy is grazing in paddock k, then she makes a sequence of k hops from a
       paddock to an adjacent paddock. The first of the k hops is always to the right,
       unless Skippy is in paddock n, in which case it is to the left. Each of the following
       k − 1 hops is in the same direction as the previous hop, unless Skippy is in paddock
       1 or n. Skippy grazes in the paddock that she is in after the k th hop.

For example, if n = 8 and Skippy is grazing in paddock 3, then the next four paddocks she
grazes in are 6, 4, 8 and 2, in this order.
Skippy continues grazing in this way indefinitely. A paddock is overgrazed if Skippy eventually
grazes in it, regardless of the paddock that she starts in. Determine all n ≥ 3 for which there
is exactly one overgrazed paddock.
```

## C3 — Combinatorics

```
There are 2025 white balls and 2025 black balls arranged in a row. A balanced segment
is a contiguous nonempty segment of balls that contains the same number of white balls as black
balls. A balanced removal is the operation of selecting a balanced segment S, removing all the
balls in S, and shifting left the balls that were to the right of S so that the remaining balls
form a contiguous row.
Determine the smallest positive integer N satisfying the following property: for every config-
uration of balls and for every integer k satisfying 0 ≤ k ≤ 2025, there exists a sequence of at
most N balanced removals after which there are exactly 2k remaining balls.
```

## C4 — Combinatorics

```
Bluey is placing lollies on a 1000 ˆ 1000 grid. Initially, every cell of the grid is empty.
At each step, Bluey chooses a row or column in which the total number of lollies is a multiple
of 3, chooses an empty cell in this row or column, and places a lolly in it. If there is no such
row or column, Bluey stops.
Determine the maximum number of lollies that Bluey can place.

Shortlisted problems                                                                                      5
```

## C5 — Combinatorics  (Germany)

```
Let n be a positive integer, and let pa1 , a2 , . . . , an q be any n-tuple of distinct integers.
An inversion is a pair pi, jq of integers satisfying 1 ≤ i < j ≤ n and ai > aj . An inversion pi, jq
is called odd if j − i is odd. Let A be the number of all inversions, and let B be the number of
odd inversions.

(a) Prove that A ≤ 5B for all n and all n-tuples pa1 , a2 , . . . , an q.

(b) Prove that there exist an n and an n-tuple pa1 , a2 , . . . , an q for which A > 4.99B.

                                                                                               (Germany)
```

## C6 — Combinatorics  (Spain)

```
On a 45 ˆ 45 square grid there is an echidna. From any cell, the echidna can move
to any other cell that shares a side. The echidna makes a sequence of 2024 moves, after which
it has visited each cell exactly once. Prove that it is possible to write the numbers from 1 to
2025, one in each cell, in such a way that:

   • For any pair of adjacent cells in the same row, the cell containing the larger number was
     visited earlier.

   • For any pair of adjacent cells in the same column, the cell containing the larger number
     was visited later.

                                                                                                   (Spain)
```

## C7 — Combinatorics

```
Let P be a regular 100-gon. An Aussie triangulation is formed by dividing P into a
set T of non-overlapping triangles such that:

   • there are exactly 2025 different points, including the 100 vertices of P , that are a vertex
     of at least one triangle in T , and

   • no three of these 2025 points are collinear.

A quokkalateral is a convex quadrilateral that consists of two triangles in T sharing a common
side. Two quokkalaterals may share a triangle in T .
Determine the minimum number of quokkalaterals among all Aussie triangulations.
```

## C8 — Combinatorics

```
Consider a 2025 ˆ 2025 grid of unit squares. We place on the grid some number of
rectangular tiles, possibly of different sizes, such that each side of every tile lies on a grid line
and every unit square is covered by at most one tile.
Determine the minimum number of tiles we need to place so that each row and each column
has exactly one unit square that is not covered by any tile.

6                                        Sunshine Coast QLD, Australia, 10th –20th July 2025
```

## G1 — Geometry

```
Let ABC be a triangle such that =A is obtuse. Let D and E be points on sides AB
and AC, respectively, such that BDEC is cyclic. Suppose the circumcircle of triangle ADE
intersects side BC at two points X and Y , where B, X, Y and C lie in that order. Let the
circumcircles of triangles BDX and CEY be Ω and Γ, respectively. Let P be a point such that
P D is tangent to Ω and P E is tangent to Γ. Let Q be a point such that QB is tangent to Ω
and QC is tangent to Γ.
Prove that points A, P and Q are collinear.
```

## G2 — Geometry

```
Let ABC be an acute-angled triangle. Let IB and IC be the excentres of triangle
ABC opposite B and C, respectively. Let E be a point on line BA such that =EIB B = 90˝ .
Let F be a point on line CA such that =CIC F = 90˝ . Let the circle with centre IB and radius
IB E intersect the segment IB B at X. Let the circle with centre IC and radius IC F intersect
the segment IC C at Y .
Prove that BY is perpendicular to CX.

The excentre of a triangle ABC opposite vertex B is the centre of the circle that is tangent to
line segment AC, to ray BA beyond A, and to ray BC beyond C. The excentre opposite C is
similarly defined.
```

## G3 — Geometry  (Kosovo)

```
Let ABC be an acute-angled triangle with AB < AC. Let Γ be the circumcircle of
triangle ABC. The perpendicular from B to AC intersects Γ again at D ‰ B. Let Q be the
point on Γ such that Q ‰ B and AB = AQ. Lines BQ and AC intersect at R. Line DR
intersects Γ again at S ‰ D. Segment BC intersects the circumcircle of triangle QRS at T .
Lines T Q and RS intersect at X.
Prove that CX is perpendicular to AB.
                                                                                 (Kosovo)
```

## G4 — Geometry  (Vietnam)

```
Let Ω and Γ be circles centred at M and N , respectively, such that the radius of Ω
is smaller than the radius of Γ. Suppose circles Ω and Γ intersect at two distinct points A and
B. Line M N intersects Ω at C and Γ at D, such that points C, M , N and D lie on the line in
that order. Let P be the circumcentre of triangle ACD. Line AP intersects Ω again at E ‰ A.
Line AP intersects Γ again at F ‰ A. Let H be the orthocentre of triangle P M N .
Prove that the line passing through H parallel to AP is tangent to the circumcircle of trian-
gle BEF .
                                                                                     (Vietnam)
```

## G5 — Geometry

```
Let ABCD be a convex quadrilateral with =ADC > 90˝ . Suppose that points X and
Y lie on diagonal AC such that

          =ADX = =Y DC = 90˝ ,        =CAD = =CBX,         and =DCA = =Y BA.

Let O be the circumcentre of triangle BXY . Suppose point R ‰ O lies on the perpendicular
bisector of AC such that lines OR and AC are parallel.
Prove that line RO bisects angle =DRB.

Shortlisted problems                                                                           7
```

## G6 — Geometry

```
Let ABC be a triangle with =B > =A > =C. Let Ω be the circumcircle of tri-
angle ABC. The lines tangent to Ω at points B and C intersect at P . Lines BP and AC
intersect at E. Lines CP and AB intersect at F . Let D be the reflection of point A in line
EF . The circumcircles of triangles DEB and DF C intersect again at Q ‰ D. Lines DP and
BC intersect at Z.
Prove that points A, Z and Q are collinear.
```

## G7 — Geometry

```
Let ABCD be a cyclic quadrilateral with circumcircle Ω such that CD > BD > BC.
The tangents to Ω at B and C meet at a point S. A line ℓ is called coastal if:

   • ℓ does not pass through A,

   • ℓ intersects ray SD at a point Xℓ beyond D, and

   • there is a circle tangent to line ℓ, line Xℓ A, segment SB and segment SC.

Prove that there is a circle that is tangent to Ω and all coastal lines.

8                                                     Sunshine Coast QLD, Australia, 10th –20th July 2025
```

## N1 — Number Theory

```
Let n and k be positive integers such that n < k < 2n. Suppose a1 , a2 , . . . , ak are
positive integers such that 2a1 + 2a2 + ··· + 2ak is divisible by 2n − 1.
Show that at least three of a1 , a2 , . . . , ak have the same remainder when divided by n.
```

## N2 — Number Theory

```
In an n ˆ n board, for each 1 ≤ i ≤ n and 1 ≤ j ≤ n, the cell in the ith row from the
bottom and j th column from the left contains gcdpi, jq leaves. A koala travels from the bottom
left corner to the top right corner. At each step, the koala moves up or to the right by a single
cell. The koala eats the leaves in each cell it visits, including the bottom left and top right
cells.
Determine the maximum number of leaves that the koala can eat.
```

## N3 — Number Theory  (Lithuania)

```
An infinite sequence a1 , a2 , . . . consists of positive integers, each of which has at least
four positive divisors. For each n ≥ 1, an+1 is the sum of the three largest proper divisors of an .
Determine all possible values of a1 .

A proper divisor of a positive integer N is a divisor of N other than N .
                                                                                                           (Lithuania)
```

## N4 — Number Theory  (Croatia)

```
Let Z>0 be the set of positive integers. Determine all functions f : Z>0 → Z such that
for every n P Z>0 , and every positive divisor d of n, there exists a positive divisor e of n such
that n divides d + f peq.
                                                                                         (Croatia)
```

## N5 — Number Theory

```
The sequence of triples of positive integers pa0 , b0 , c0 q, pa1 , b1 , c1 q, . . . , pa2025 , b2025 , c2025 q
satisfies                                +                                                          ˘
                  pai+1 , bi+1 , ci+1 q = ai + gcdpbi , ci q, bi + gcdpci , ai q, ci + gcdpai , bi q
for 0 ≤ i ≤ 2024.
Determine the smallest possible value of a2025 .
```

## N6 — Number Theory

```
For positive integers n and k, let fk pnq denote the remainder when n is divided by
    k
2 − 1. A positive integer n is grouse if

                                     f1 pnq ≤ f2 pnq ≤ f3 pnq ≤ f4 pnq ≤ ··· .

    (a) Prove that there are infinitely many grouse numbers.

    (b) Prove that there exists a positive integer M such that there are at most M {20252025
        grouse numbers less than M .

Shortlisted problems                                                                        9
```

## N7 — Number Theory

```
Let Z>0 denote the set of positive integers. A function f : Z>0 → Z>0 is said to be
bonza if
                                  f paq divides ba − f pbqf paq
for all positive integers a and b.
Determine the smallest constant c such that f pnq ≤ cn for any bonza function f and any
positive integer n.
```

## N8 — Number Theory

```
Prove that there are finitely many prime numbers p such that

   • p − 8 is a perfect square, and
   • for all odd positive integers k <    p, the number p − k 2 has at most two distinct prime
     factors.

10                                          Sunshine Coast QLD, Australia, 10th –20th July 2025

                                       Solutions
 A1.      Quadratic solitaire is a single-player game. To start the game, the player chooses two
distinct nonzero integers a and b and writes the equation x2 + ax + b = 0 on a blackboard. On
each turn, if the equation currently written on the blackboard has two distinct nonzero integer
solutions x = u and x = v, then the player erases the equation and replaces it by one of the
equations x2 + ux + v = 0 or x2 + vx + u = 0 of their choosing. Otherwise, the game ends.
    Determine all initial choices of a and b such that quadratic solitaire can be played forever.

Answer: The only pair pa, bq for which quadratic solitaire can be played forever is p1, −2q.
```
