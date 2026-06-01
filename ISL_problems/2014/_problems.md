# IMO Shortlist 2014 problems
_fidelity: approx (math glyphs recovered best-effort)_

## A1 — Algebra

```
Let z0 < z1 < z2 < ··· be an infinite sequence of positive integers. Prove that there
exists a unique integer n ≥ 1 such that
                                         z0 + z1 + ··· + zn
                                  zn <                        ≤ zn+1 .
```

## A2 — Algebra  (Denmark)

```
Define the function f : p0, 1q → p0, 1q by
                                              x + 12     if x < 21 ,
                                     f pxq =
                                              x2         if x ≥ 21 .

Let a and b be two real numbers such that 0 < a < b < 1. We define the sequences an and bn
by a0 = a, b0 = b, and an = f pan−1 q, bn = f pbn−1 q for n > 0. Show that there exists a positive
integer n such that
                                  pan − an−1 qpbn − bn−1 q < 0.
                                                                                       (Denmark)
```

## A3 — Algebra

```
For a sequence x1 , x2 , . . . , xn of real numbers, we define its price as
                                         max |x1 + ··· + xi |.
                                         1≤i≤n

    Given n real numbers, Dave and George want to arrange them into a sequence with a
low price. Diligent Dave checks all possible ways and finds the minimum possible price D.
Greedy George, on the other hand, chooses x1 such that |x1 | is as small as possible; among
the remaining numbers, he chooses x2 such that |x1 + x2 | is as small as possible, and so on.
Thus, in the ith step he chooses xi among the remaining numbers so as to minimise the value
of |x1 + x2 + ··· + xi |. In each step, if several numbers provide the same value, George chooses
one at random. Finally he gets a sequence with price G.
    Find the least possible constant c such that for every positive integer n, for every collection
of n real numbers, and for every possible sequence that George might obtain, the resulting
values satisfy the inequality G ≤ cD.
```

## A4 — Algebra  (Netherlands)

```
Determine all functions f : Z → Z satisfying
                             +         ˘
                            f f pmq + n + f pmq = f pnq + f p3mq + 2014
for all integers m and n.
                                                                                    (Netherlands)

Shortlisted problems                                                                            5
```

## A5 — Algebra

```
Consider all polynomials P pxq with real coefficients that have the following property:
for any two real numbers x and y one has

                   |y 2 − P pxq| ≤ 2 |x| if and only if |x2 − P pyq| ≤ 2 |y| .

   Determine all possible values of P p0q.
```

## A6 — Algebra

```
Find all functions f : Z → Z such that
                                    n2 + 4f pnq = f pf pnqq2

for all n P Z.

6                                                                       IMO 2014 South Africa
```

## C1 — Combinatorics

```
Let n points be given inside a rectangle R such that no two of them lie on a line parallel
to one of the sides of R. The rectangle R is to be dissected into smaller rectangles with sides
parallel to the sides of R in such a way that none of these rectangles contains any of the given
points in its interior. Prove that we have to dissect R into at least n + 1 smaller rectangles.
```

## C2 — Combinatorics

```
We have 2 sheets of paper, with the number 1 written on each of them. We perform

the following operation. In every step we choose two distinct sheets; if the numbers on the two
sheets are a and b, then we erase these numbers and write the number a + b on both sheets.
Prove that after m2m−1 steps, the sum of the numbers on all the sheets is at least 4m .
```

## C3 — Combinatorics  (Croatia)

```
Let n ≥ 2 be an integer. Consider an n ˆ n chessboard divided into n2 unit squares.
We call a configuration of n rooks on this board happy if every row and every column contains
exactly one rook. Find the greatest positive integer k such that for every happy configuration
of rooks, we can find a k ˆ k square without a rook on any of its k 2 unit squares.
                                                                                        (Croatia)
```

## C4 — Combinatorics

```
Construct a tetromino by attaching two 2 ˆ 1 dominoes along their longer sides such
that the midpoint of the longer side of one domino is a corner of the other domino. This
construction yields two kinds of tetrominoes with opposite orientations. Let us call them S-
and Z-tetrominoes, respectively.

                           S-tetrominoes               Z-tetrominoes

    Assume that a lattice polygon P can be tiled with S-tetrominoes. Prove than no matter
how we tile P using only S- and Z-tetrominoes, we always use an even number of Z-tetrominoes.
```

## C5 — Combinatorics

```
Consider n ≥ 3 lines in the plane such that no two lines are parallel and no three have a
common point. These lines divide the plane into polygonal
                                                        Pa regions;
                                                             T      let F be the set of regions
having finite area. Prove that it is possible to colour   n{2 of the lines blue in such a way
that no region in F has a completely blue boundary. (For a real number x, rxs denotes the
least integer which is not smaller than x.)

Shortlisted problems                                                                             7
```

## C6 — Combinatorics

```
We are given an infinite deck of cards, each with a real number on it. For every real
number x, there is exactly one card in the deck that has x written on it. Now two players draw
disjoint sets A and B of 100 cards each from this deck. We would like to define a rule that
declares one of them a winner. This rule should satisfy the following conditions:

  1. The winner only depends on the relative order of the 200 cards: if the cards are laid down
     in increasing order face down and we are told which card belongs to which player, but
     not what numbers are written on them, we can still decide the winner.

  2. If we write the elements of both sets in increasing order as A = ta1 , a2 , . . . , a100 u and
     B = tb1 , b2 , . . . , b100 u, and ai > bi for all i, then A beats B.

  3. If three players draw three disjoint sets A, B, C from the deck, A beats B and B beats C,
     then A also beats C.

How many ways are there to define such a rule? Here, we consider two rules as different if there
exist two sets A and B such that A beats B according to one rule, but B beats A according to
the other.
```

## C7 — Combinatorics

```
Let M be a set of n ≥ 4 points in the plane, no three of which are collinear. Initially these
points are connected with n segments so that each point in M is the endpoint of exactly two
segments. Then, at each step, one may choose two segments AB and CD sharing a common
interior point and replace them by the segments AC and BD if none of them is present at this
moment. Prove that it is impossible to perform n3 {4 or more such moves.
```

## C8 — Combinatorics

```
A card deck consists of 1024 cards. On each card, a set of distinct decimal digits is
written in such a way that no two of these sets coincide (thus, one of the cards is empty). Two
players alternately take cards from the deck, one card per turn. After the deck is empty, each
player checks if he can throw out one of his cards so that each of the ten digits occurs on an
even number of his remaining cards. If one player can do this but the other one cannot, the
one who can is the winner; otherwise a draw is declared.
    Determine all possible first moves of the first player after which he has a winning strategy.
```

## C9 — Combinatorics  (India)

```
There are n circles drawn on a piece of paper in such a way that any two circles
intersect in two points, and no three circles pass through the same point. Turbo the snail slides
along the circles in the following fashion. Initially he moves on one of the circles in clockwise
direction. Turbo always keeps sliding along the current circle until he reaches an intersection
with another circle. Then he continues his journey on this new circle and also changes the
direction of moving, i.e. from clockwise to anticlockwise or vice versa.
    Suppose that Turbo’s path entirely covers all circles. Prove that n must be odd.
                                                                                          (India)

8                                                                     IMO 2014 South Africa
```

## G1 — Geometry

```
The points P and Q are chosen on the side BC of an acute-angled triangle ABC so
that =P AB = =ACB and =QAC = =CBA. The points M and N are taken on the rays AP
and AQ, respectively, so that AP = P M and AQ = QN. Prove that the lines BM and CN
intersect on the circumcircle of the triangle ABC.
```

## G2 — Geometry  (Estonia)

```
Let ABC be a triangle. The points K, L, and M lie on the segments BC, CA, and AB,
respectively, such that the lines AK, BL, and CM intersect in a common point. Prove that it
is possible to choose two of the triangles ALM, BMK, and CKL whose inradii sum up to at
least the inradius of the triangle ABC.
                                                                                 (Estonia)
```

## G3 — Geometry  (Here we always assume that an angle bisector is a ray.)

```
Let Ω and O be the circumcircle and the circumcentre of an acute-angled triangle ABC
with AB > BC. The angle bisector of =ABC intersects Ω at M ‰ B. Let Γ be the circle
with diameter BM. The angle bisectors of =AOB and =BOC intersect Γ at points P and Q,
respectively. The point R is chosen on the line P Q so that BR = MR. Prove that BR k AC.
(Here we always assume that an angle bisector is a ray.)
```

## G4 — Geometry

```
Consider a fixed circle Γ with three fixed points A, B, and C on it. Also, let us fix
a real number λ P p0, 1q. For a variable point P R tA, B, Cu on Γ, let M be the point on
the segment CP such that CM = λ · CP . Let Q be the second point of intersection of the
circumcircles of the triangles AMP and BMC. Prove that as P varies, the point Q lies on a
fixed circle.
```

## G5 — Geometry

```
Let ABCD be a convex quadrilateral with =B = =D = 90 . Point H is the foot of
                                                                   ˝

the perpendicular from A to BD. The points S and T are chosen on the sides AB and AD,
respectively, in such a way that H lies inside triangle SCT and

                     =SHC − =BSC = 90˝ ,       =T HC − =DT C = 90˝ .

Prove that the circumcircle of triangle SHT is tangent to the line BD.
```

## G6 — Geometry

```
Let ABC be a fixed acute-angled triangle. Consider some points E and F lying on
the sides AC and AB, respectively, and let M be the midpoint of EF . Let the perpendicular
bisector of EF intersect the line BC at K, and let the perpendicular bisector of MK intersect
the lines AC and AB at S and T , respectively. We call the pair pE, F q interesting, if the
quadrilateral KSAT is cyclic.
    Suppose that the pairs pE1 , F1 q and pE2 , F2 q are interesting. Prove that
                                       E1 E2   F1 F2
                                             =       .
                                       AB      AC
```

## G7 — Geometry

```
Let ABC be a triangle with circumcircle Ω and incentre I. Let the line passing through I
and perpendicular to CI intersect the segment BC and the arc BC (not containing A) of Ω at
points U and V , respectively. Let the line passing through U and parallel to AI intersect AV
at X, and let the line passing through V and parallel to AI intersect AB at Y . Let W and Z be
the midpoints of AX and BC, respectively. Prove that if the points I, X, and Y are collinear,
then the points I, W , and Z are also collinear.

Shortlisted problems                                                                                  9
```

## N1 — Number Theory

```
Let n ≥ 2 be an integer, and let An be the set
                                 An = t2n − 2k | k P Z, 0 ≤ k < nu.

Determine the largest positive integer that cannot be written as the sum of one or more (not
necessarily distinct) elements of An .
```

## N2 — Number Theory

```
Determine all pairs px, yq of positive integers such that
                               a3
                                  7x2 − 13xy + 7y 2 = |x − y| + 1 .
```

## N3 — Number Theory  (Luxembourg)

```
A coin is called a Cape Town coin if its value is 1{n for some positive integer n. Given
a collection of Cape Town coins of total value at most 99 + 21 , prove that it is possible to split
this collection into at most 100 groups each of total value at most 1.
                                                                                    (Luxembourg)
```

## N4 — Number Theory  (Hong Kong)

```
Let n > 1 be a given integer. Prove that infinitely many terms of the sequence pak qk≥1 ,
defined by                                     Z k^
                                          ak =        ,
are odd. (For a real number x, txu denotes the largest integer not exceeding x.)
                                                                                          (Hong Kong)
```

## N5 — Number Theory

```
Find all triples pp, x, yq consisting of a prime number p and two positive integers x and y
such that xp−1 + y and x + y p−1 are both powers of p.
```

## N6 — Number Theory

```
Let a1 < a2 < ··· < an be pairwise coprime positive integers with a1 being prime
and a1 ≥ n + 2. On the segment I = r0, a1 a2 ··· an s of the real line, mark all integers that are
divisible by at least one of the numbers a1 , . . . , an . These points split I into a number of smaller
segments. Prove that the sum of the squares of the lengths of these segments is divisible by a1 .
```

## N7 — Number Theory

```
Let c ≥ 1 be an integer. Define a sequence of positive integers by a1 = c and
                                  an+1 = a3n − 4c · a2n + 5c2 · an + c

for all n ≥ 1. Prove that for each integer n ≥ 2 there exists a prime number p dividing an but
none of the numbers a1 , . . . , an−1 .
```

## N8 — Number Theory

```
For every real number x, let }x} denote the distance between x and the nearest integer.
Prove that for every pair pa, bq of positive integers there exist an odd prime p and a positive
integer k satisfying                    › › › › ›          ›
                                        › a › › b › ›a + b›
                                        › ›+› ›+›
                                        › pk › › pk › › pk › = 1.
                                                           ›

10                                                                            IMO 2014 South Africa

                                        Solutions

A1.     Let z0 < z1 < z2 < ··· be an infinite sequence of positive integers. Prove that there
exists a unique integer n ≥ 1 such that
                                          z0 + z1 + ··· + zn
                                   zn <                        ≤ zn+1 .                            p1q
```
