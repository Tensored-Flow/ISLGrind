# IMO Shortlist 2007 problems
_fidelity: exact_

## A1 — Algebra  (New Zealand)

```
Given a sequence a1 , a2 , . . . , an of real numbers. For each i (1 ≤ i ≤ n) define
                         di = max{aj : 1 ≤ j ≤ i} − min{aj : i ≤ j ≤ n}

and let
                                    d = max{di : 1 ≤ i ≤ n}.
(a) Prove that for arbitrary real numbers x1 ≤ x2 ≤ . . . ≤ xn ,
                                                           d
                                max |xi − ai | : 1 ≤ i ≤ n ≥ .                               (1)
(b) Show that there exists a sequence x1 ≤ x2 ≤ . . . ≤ xn of real numbers such that we have
equality in (1).
                                                                              (New Zealand)
```

## A2 — Algebra  (N denotes the set of all positive integers.)

```
Consider those functions f : N → N which satisfy the condition
                                  f (m + n) ≥ f (m) + f f (n) − 1                                 (1)
for all m, n ∈ N. Find all possible values of f (2007).
    (N denotes the set of all positive integers.)
                                                                                          (Bulgaria)
Answer. 1, 2, . . . , 2008.
```

## A3 — Algebra  (Estonia)

```
Let n be a positive integer, and let x and y be positive real numbers such that xn +y n = 1.
Prove that                                       !                        !
                              n                       n
                              X 1 + x2k               X 1 + y 2k                        1
                                                                              <                  .
                                     1 + x4k          k=1
                                                              1 + y 4k            (1 − x)(1 − y)
                                                                                                                         (Estonia)
```

## A4 — Algebra  (Thaliand)

```
Find all functions f : R+ → R+ such that
                                f x + f (y) = f (x + y) + f (y)                              (1)

for all x, y ∈ R+ . (Symbol R+ denotes the set of all positive real numbers.)
                                                                                     (Thaliand)
Answer. f (x) = 2x.
                                                            +
```

## A5 — Algebra  (Croatia)

```
Let c > 2, and let a(1), a(2), . . . be a sequence of nonnegative real numbers such that
                                a(m + n) ≤ 2a(m) + 2a(n) for all m, n ≥ 1,                                          (1)

                                         a(2k ) ≤                      for all k ≥ 0.                               (2)
                                                     (k + 1)c
Prove that the sequence a(n) is bounded.
                                                                                                              (Croatia)
```

## A6 — Algebra  (Poland)

```
Let a1 , a2 , . . . , a100 be nonnegative real numbers such that a21 + a22 + . . . + a2100 = 1. Prove
that
                                              a21 a2 + a22 a3 + . . . + a2100 a1 <                   .
                                                                                                                                          (Poland)
```

## A7 — Algebra  (Netherlands)

```
Let n > 1 be an integer. In the space, consider the set
                          S = (x, y, z) | x, y, z ∈ {0, 1, . . . , n}, x + y + z > 0 .

Find the smallest number of planes that jointly contain all (n + 1)3 − 1 points of S but none of
them passes through the origin.
                                                                                   (Netherlands)
Answer. 3n planes.
```

## C1 — Combinatorics  (Serbia)

```
Let n > 1 be an integer. Find all sequences a1 , a2 , . . . , an2 +n satisfying the following
conditions:
   (a) ai ∈ {0, 1} for all 1 ≤ i ≤ n2 + n;
   (b) ai+1 + ai+2 + . . . + ai+n < ai+n+1 + ai+n+2 + . . . + ai+2n for all 0 ≤ i ≤ n2 − n.
                                                                                             (Serbia)
Answer. Such a sequence is unique. It can be defined as follows:
                     0, u + v ≤ n,
          au+vn =                           for all 1 ≤ u ≤ n and 0 ≤ v ≤ n.                                             (1)
                     1, u + v ≥ n + 1

The terms can be arranged into blocks of length n as

         (0| .{z
               . . 0)
                   } (0| .{z
                           . . 0} 1) (0| .{z
                                           . . 0} 1 1) . . . (|0 .{z
                                                                   . . 0} |1 .{z
                                                                               . . 1)
                                                                                   } . . . (0 1| .{z
                                                                                                   . . 1)
                                                                                                       } (|1 .{z
                                                                                                               . . 1).
                                                                                                                   }
              n          n−1             n−2                   n−v             v              n−1             n
```

## C2 — Combinatorics  (Japan)

```
A unit square is dissected into n > 1 rectangles such that their sides are parallel to the
sides of the square. Any line, parallel to a side of the square and intersecting its interior, also
intersects the interior of some rectangle. Prove that in this dissection, there exists a rectangle
having no point on the boundary of the square.
                                                                                          (Japan)
```

## C3 — Combinatorics  (Netherlands)

```
Find all positive integers n, for which the numbers in the set S = {1, 2, . . . , n} can be
colored red and blue, with the following condition being satisfied: the set S × S × S contains
exactly 2007 ordered triples (x, y, z) such that (i) x, y, z are of the same color and (ii) x + y + z
is divisible by n.
                                                                                      (Netherlands)
Answer. n = 69 and n = 84.
```

## C4 — Combinatorics  (Iran)

```
Let A0 = (a1 , . . . , an) be a finite sequence of real numbers. For each k ≥ 0, from the
sequence Ak = (x1 , . . . , xn ) we construct a new sequence Ak+1 in the following way.
   1. We choose a partition {1, . . . , n} = I ∪ J, where I and J are two disjoint sets, such that
the expression
                                             X        X
                                                 xi −   xj
                                                        i∈I            j∈J

attains the smallest possible value. (We allow the sets I or J to be empty; in this case the
corresponding sum is 0.) If there are several such partitions, one is chosen arbitrarily.
   2. We set Ak+1 = (y1 , . . . , yn ), where yi = xi + 1 if i ∈ I, and yi = xi − 1 if i ∈ J.
   Prove that for some k, the sequence Ak contains an element x such that |x| ≥ n/2.
                                                                                              (Iran)
```

## C5 — Combinatorics  (Romania)

```
In the Cartesian coordinate plane define the strip Sn = {(x, y) | n ≤ x < n + 1} for
every integer n. Assume that each strip Sn is colored either red or blue, and let a and b be two
distinct positive integers. Prove that there exists a rectangle with side lengths a and b such
that its vertices have the same color.
                                                                                      (Romania)
```

## C6 — Combinatorics  (Russia)

```
In a mathematical competition some competitors are friends; friendship is always mutual.
Call a group of competitors a clique if each two of them are friends. The number of members
in a clique is called its size.
    It is known that the largest size of cliques is even. Prove that the competitors can be
arranged in two rooms such that the largest size of cliques in one room is the same as the
largest size of cliques in the other room.
                                                                                    (Russia)
```

## C7 — Combinatorics  (Austria)

```
Let α <                   be a positive real number. Prove that there exist positive integers n
and p > α · 2 for which one can select 2p pairwise distinct subsets S1 , . . . , Sp , T1 , . . . , Tp of
the set {1, 2, . . . , n} such that Si ∩ Tj 6= ∅ for all 1 ≤ i, j ≤ p.
                                                                                           (Austria)
```

## C8 — Combinatorics  (Ukraine)

```
Given a convex n-gon P in the plane. For every three vertices of P , consider the triangle
determined by them. Call such a triangle good if all its sides are of unit length.
   Prove that there are not more than 23 n good triangles.
                                                                                    (Ukraine)
```

## G1 — Geometry  (Czech Republic)

```
In triangle ABC, the angle bisector at vertex C intersects the circumcircle and the per-
pendicular bisectors of sides BC and CA at points R, P , and Q, respectively. The midpoints of
BC and CA are S and T , respectively. Prove that triangles RQT and RP S have the same area.
                                                                              (Czech Republic)
```

## G2 — Geometry  (Canada)

```
Given an isosceles triangle ABC with AB = AC. The midpoint of side BC is denoted
by M. Let X be a variable point on the shorter arc MA of the circumcircle of triangle ABM.
Let T be the point in the angle domain BMA, for which ∠T MX = 90◦ and T X = BX. Prove
that ∠MT B − ∠CT M does not depend on X.
                                                                                   (Canada)
```

## G3 — Geometry  (Ukraine)

```
The diagonals of a trapezoid ABCD intersect at point P . Point Q lies between the
parallel lines BC and AD such that ∠AQD = ∠CQB, and line CD separates points P and Q.
Prove that ∠BQP = ∠DAQ.
                                                                                   (Ukraine)
                   AD
```

## G4 — Geometry  (Luxembourg)

```
Consider five points A, B, C, D, E such that ABCD is a parallelogram and BCED is
a cyclic quadrilateral. Let ` be a line passing through A, and let ` intersect segment DC and
line BC at points F and G, respectively. Suppose that EF = EG = EC. Prove that ` is the
bisector of angle DAB.
                                                                                  (Luxembourg)
```

## G5 — Geometry  (United Kingdom)

```
Let ABC be a fixed triangle, and let A1 , B1 , C1 be the midpoints of sides BC, CA, AB,
respectively. Let P be a variable point on the circumcircle. Let lines P A1 , P B1 , P C1 meet the
circumcircle again at A0 , B 0 , C 0 respectively. Assume that the points A, B, C, A0 , B 0 , C 0 are
distinct, and lines AA0 , BB 0 , CC 0 form a triangle. Prove that the area of this triangle does not
depend on P .
                                                                                 (United Kingdom)
```

## G6 — Geometry  (U.S.A.)

```
Determine the smallest positive real number k with the following property.
    Let ABCD be a convex quadrilateral, and let points A1 , B1 , C1 and D1 lie on sides AB, BC,
CD and DA, respectively. Consider the areas of triangles AA1 D1 , BB1 A1 , CC1 B1 , and DD1 C1 ;
let S be the sum of the two smallest ones, and let S1 be the area of quadrilateral A1 B1 C1 D1 .
Then we always have kS1 ≥ S.
                                                                                        (U.S.A.)
Answer. k = 1.
```

## G7 — Geometry  (Iran)

```
Given an acute triangle ABC with angles α, β and γ at vertices A, B and C, respectively,
such that β > γ. Point I is the incenter, and R is the circumradius. Point D is the foot of
the altitude from vertex A. Point K lies on line AD such that AK = 2R, and D separates A
and K. Finally, lines DI and KI meet sides AC and BC at E and F , respectively.
   Prove that if IE = IF then β ≤ 3γ.
                                                                                     (Iran)
```

## G8 — Geometry  (Poland)

```
Point P lies on side AB of a convex quadrilateral ABCD. Let ω be the incircle
of triangle CP D, and let I be its incenter. Suppose that ω is tangent to the incircles of
triangles AP D and BP C at points K and L, respectively. Let lines AC and BD meet at E,
and let lines AK and BL meet at F . Prove that points E, I, and F are collinear.
                                                                                 (Poland)
```

## N1 — Number Theory  (Austria)

```
Find all pairs (k, n) of positive integers for which 7k − 3n divides k4 + n2 .
                                                                                        (Austria)
Answer. (2, 4).
```

## N2 — Number Theory  (Canada)

```
Let b, n > 1 be integers. Suppose that for each k > 1 there exists an integer ak such
that b − ank is divisible by k. Prove that b = An for some integer A.
                                                                                (Canada)
```

## N3 — Number Theory  (Netherlands)

```
Let X be a set of 10 000 integers, none of them is divisible by 47. Prove that there
exists a 2007-element subset Y of X such that a − b + c − d + e is not divisible by 47 for any
a, b, c, d, e ∈ Y .
                                                                                 (Netherlands)
```

## N4 — Number Theory  (Poland)

```
For every integer k ≥ 2, prove that 23k divides the number
                                               k+1  k 
                                               2       2
                                                    − k−1                                                      (1)
                                                2     2

but 23k+1 does not.
                                                                                                         (Poland)
```

## N5 — Number Theory  (N is the set of all positive integers.)

```
Find all surjective functions f : N → N such that for every m, n ∈ N and every prime p,
the number f (m + n) is divisible by p if and only if f (m) + f (n) is divisible by p.
   (N is the set of all positive integers.)
                                                                                                (Iran)
Answer. f (n) = n.
```

## N6 — Number Theory  (United Kingdom)

```
Let k be a positive integer. Prove that the number (4k2 − 1)2 has a positive divisor of
the form 8kn − 1 if and only if k is even.
                                                                                (United Kingdom)
```

## N7 — Number Theory  (India)

```
For a prime p and a positive integer n, denote by νp (n) the exponent of p in the prime
factorization of n!. Given a positive integer d and a finite set {p1 , . . . , pk } of primes. Show that
there are infinitely many positive integers n such that d νpi (n) for all 1 ≤ i ≤ k.
                                                                                                 (India)
```
