# IMO Shortlist 2023 problems
_fidelity: approx (math glyphs recovered best-effort)_

## A1 — Algebra

```
Professor Oak is feeding his 100 Pokémon. Each Pokémon has a bowl whose capacity
is a positive real number of kilograms. These capacities are known to Professor Oak. The total
capacity of all the bowls is 100 kilograms. Professor Oak distributes 100 kilograms of food in
such a way that each Pokémon receives a non-negative integer number of kilograms of food
(which may be larger than the capacity of their bowl). The dissatisfaction level of a Pokémon
who received N kilograms of food and whose bowl has a capacity of C kilograms is equal to
|N − C|.
    Find the smallest real number D such that, regardless of the capacities of the bowls, Pro-
fessor Oak can distribute the food in a way that the sum of the dissatisfaction levels over all
the 100 Pokémon is at most D.
```

## A2 — Algebra

```
Let R be the set of real numbers. Let f : R → R be a function such that

                                     f px + yqf px − yq ≥ f pxq2 − f pyq2

for every x, y P R. Assume that the inequality is strict for some x0 , y0 P R.
    Prove that f pxq ≥ 0 for every x P R or f pxq ≤ 0 for every x P R.
```

## A3 — Algebra

```
Let x1 , x2 , . . . , x2023 be distinct real positive numbers such that
                                     d                       ˆ                    ˙
                                                                1    1         1
                             an = px1 + x2 + ··· + xn q         +    + ··· +
                                                               x1 x 2          xn

is an integer for every n = 1, 2, . . . , 2023. Prove that a2023 ≥ 3034.
```

## A4 — Algebra  (Belgium)

```
Let R>0 be the set of positive real numbers. Determine all functions f : R>0 → R>0
such that                           +             ˘ +             ˘
                                   x f pxq + f pyq ≥ f pf pxqq + y f pyq
for every x, y P R>0 .
                                                                                                   (Belgium)
```

## A5 — Algebra  (Australia)

```
Let a1 , a2 , . . . , a2023 be positive integers such that

    • a1 , a2 , . . . , a2023 is a permutation of 1, 2, . . . , 2023, and

   • |a1 − a2 |, |a2 − a3 |, . . . , |a2022 − a2023 | is a permutation of 1, 2, . . . , 2022.

Prove that max a1 , a2023 ≥ 507.
                  +          ˘

                                                                                                  (Australia)

4                                                                    Chiba, Japan, 2nd–13th July 2023
```

## A6 — Algebra

```
Let k ≥ 2 be an integer. Determine all sequences of positive integers a1 , a2 , . . . for
which there exists a monic polynomial P of degree k with non-negative integer coefficients such
                                 P pan q = an+1 an+2 ··· an+k
for every integer n ≥ 1.
```

## A7 — Algebra

```
Let N be a positive integer. Prove that there exist three permutations a1 , a2 , . . . , aN ;
b1 , b2 , . . . , bN ; and c1 , c2 , . . . , cN of 1, 2, . . . , N such that
                                               ?       a          ?       ?
                                                 ak + bk + ck − 2 N < 2023

for every k = 1, 2, . . . , N .

Shortlisted problems                                                                               5
```

## C1 — Combinatorics  (Thailand)

```
Let m and n be positive integers greater than 1. In each unit square of an m ˆ n grid
lies a coin with its tail-side up. A move consists of the following steps:

  1. select a 2 ˆ 2 square in the grid;

  2. flip the coins in the top-left and bottom-right unit squares;

  3. flip the coin in either the top-right or bottom-left unit square.

Determine all pairs pm, nq for which it is possible that every coin shows head-side up after a
finite number of moves.
                                                                                   (Thailand)
```

## C2 — Combinatorics  (Czech Republic)

```
Determine the maximal length L of a sequence a1 , . . . , aL of positive integers satisfying
both the following properties:

   • every term in the sequence is less than or equal to 22023 , and

   • there does not exist a consecutive subsequence ai , ai+1 , . . . , aj (where 1 ≤ i ≤ j ≤ L) with
     a choice of signs si , si+1 , . . . , sj P t1, −1u for which

                                    si ai + si+1 ai+1 + ··· + sj aj = 0.

                                                                                  (Czech Republic)
```

## C3 — Combinatorics

```
Let n be a positive integer. We arrange 1 + 2 + ··· + n circles in a triangle with n
rows, such that the ith row contains exactly i circles. The following figure shows the case n = 6.

                                                n=6

    In this triangle, a ninja-path is a sequence of circles obtained by repeatedly going from a
circle to one of the two circles directly below it. In terms of n, find the largest value of k such
that if one circle from every row is coloured red, we can always find a ninja-path in which at
least k of the circles are red.
```

## C4 — Combinatorics

```
Let n ≥ 2 be a positive integer. Paul has a 1 ˆ n2 rectangular strip consisting of n2
unit squares, where the ith square is labelled with i for all 1 ≤ i ≤ n2 . He wishes to cut the
strip into several pieces, where each piece consists of a number of consecutive unit squares, and
then translate (without rotating or flipping) the pieces to obtain an n ˆ n square satisfying the
following property: if the unit square in the ith row and j th column is labelled with aij , then
aij − pi + j − 1q is divisible by n.
    Determine the smallest number of pieces Paul needs to make in order to accomplish this.

6                                                               Chiba, Japan, 2nd–13th July 2023
```

## C5 — Combinatorics  (Israel)

```
Elisa has 2023 treasure chests, all of which are unlocked and empty at first. Each day,
Elisa adds a new gem to one of the unlocked chests of her choice, and afterwards, a fairy acts
according to the following rules:

     • if more than one chests are unlocked, it locks one of them, or

     • if there is only one unlocked chest, it unlocks all the chests.

Given that this process goes on forever, prove that there is a constant C with the following
property: Elisa can ensure that the difference between the numbers of gems in any two chests
never exceeds C, regardless of how the fairy chooses the chests to lock.
                                                                                     (Israel)
```

## C6 — Combinatorics

```
Let N be a positive integer, and consider an N ˆ N grid. A right-down path is a
sequence of grid cells such that each cell is either one cell to the right of or one cell below the
previous cell in the sequence. A right-up path is a sequence of grid cells such that each cell is
either one cell to the right of or one cell above the previous cell in the sequence.
    Prove that the cells of the N ˆ N grid cannot be partitioned into less than N right-down
or right-up paths. For example, the following partition of the 5 ˆ 5 grid uses 5 paths.
```

## C7 — Combinatorics

```
The Imomi archipelago consists of n ≥ 2 islands. Between each pair of distinct islands
is a unique ferry line that runs in both directions, and each ferry line is operated by one of
k companies. It is known that if any one of the k companies closes all its ferry lines, then
it becomes impossible for a traveller, no matter where the traveller starts at, to visit all the
islands exactly once (in particular, not returning to the island the traveller started at).
    Determine the maximal possible value of k in terms of n.

Shortlisted problems                                                                           7
```

## G1 — Geometry

```
Let ABCDE be a convex pentagon such that =ABC = =AED = 90˝ . Suppose
that the midpoint of CD is the circumcentre of triangle ABE. Let O be the circumcentre of
triangle ACD.
   Prove that line AO passes through the midpoint of segment BE.
```

## G2 — Geometry  (Iran)

```
Let ABC be a triangle with AC > BC. Let ω be the circumcircle of triangle ABC
and let r be the radius of ω. Point P lies on segment AC such that BC = CP and point S is
the foot of the perpendicular from P to line AB. Let ray BP intersect ω again at D and let Q
lie on line SP such that P Q = r and S, P, Q lie on the line in that order. Finally, let the line
perpendicular to CQ from A intersect the line perpendicular to DQ from B at E.
   Prove that E lies on ω.
                                                                                          (Iran)
```

## G3 — Geometry

```
Let ABCD be a cyclic quadrilateral with =BAD < =ADC. Let M be the midpoint
of the arc CD not containing A. Suppose there is a point P inside ABCD such that =ADB =
=CP D and =ADP = =P CB.
   Prove that lines AD, P M, BC are concurrent.
```

## G4 — Geometry  (Portugal)

```
Let ABC be an acute-angled triangle with AB < AC. Denote its circumcircle by Ω
and denote the midpoint of arc CAB by S. Let the perpendicular from A to BC meet BS
and Ω at D and E ‰ A respectively. Let the line through D parallel to BC meet line BE at L
and denote the circumcircle of triangle BDL by ω. Let ω meet Ω again at P ‰ B.
   Prove that the line tangent to ω at P , and line BS intersect on the internal bisector
of =BAC.
                                                                              (Portugal)
```

## G5 — Geometry

```
Let ABC be an acute-angled triangle with circumcircle ω and circumcentre O. Points
D ‰ B and E ‰ C lie on ω such that BD K AC and CE K AB. Let CO meet AB at X, and
BO meet AC at Y .
   Prove that the circumcircles of triangles BXD and CY E have an intersection on line AO.
```

## G6 — Geometry  (United Kingdom)

```
Let ABC be an acute-angled triangle with circumcircle ω. A circle Γ is internally
tangent to ω at A and also tangent to BC at D. Let AB and AC intersect Γ at P and Q
respectively. Let M and N be points on line BC such that B is the midpoint of DM and
C is the midpoint of DN . Lines M P and N Q meet at K and intersect Γ again at I and J
respectively. The ray KA meets the circumcircle of triangle IJK at X ‰ K.
   Prove that =BXP = =CXQ.
                                                                              (United Kingdom)

8                                                            Chiba, Japan, 2nd–13th July 2023
```

## G7 — Geometry

```
Let ABC be an acute, scalene triangle with orthocentre H. Let +a be the line through
the reflection of B with respect to CH and the reflection of C with respect to BH. Lines +b
and +c are defined similarly. Suppose lines +a , +b , and +c determine a triangle T .
     Prove that the orthocentre of T , the circumcentre of T and H are collinear.
```

## G8 — Geometry

```
Let ABC be an equilateral triangle. Points A1 , B1 , C1 lie inside triangle ABC such
that triangle A1 B1 C1 is scalene, BA1 = A1 C, CB1 = B1 A, AC1 = C1 B and

                             =BA1 C + =CB1 A + =AC1 B = 480˝ .

Lines BC1 and CB1 intersect at A2 ; lines CA1 and AC1 intersect at B2 ; and lines AB1 and
BA1 intersect at C2 .
     Prove that the circumcircles of triangles AA1 A2 , BB1 B2 , CC1 C2 have two common points.

Shortlisted problems                                                                                             9
```

## N1 — Number Theory  (Colombia)

```
Determine all positive, composite integers n that satisfy the following property: if
the positive divisors of n are 1 = d1 < d2 < ··· < dk = n, then di divides di+1 + di+2 for every
1 ≤ i ≤ k − 2.
                                                                                      (Colombia)
```

## N2 — Number Theory  (Bangladesh)

```
Determine all pairs pa, pq of positive integers with p prime such that pa +a4 is a perfect
square.
                                                                                                (Bangladesh)
```

## N3 — Number Theory  (Brazil)

```
For positive integers n and k ≥ 2 define Ek pnq as the greatest exponent r such that
k r divides n!. Prove that there are infinitely many n such that E10 pnq > E9 pnq and infinitely
many m such that E10 pmq < E9 pmq.
                                                                                        (Brazil)
```

## N4 — Number Theory

```
Let a1 , a2 , . . . , an , b1 , b2 , . . . , bn be 2n positive integers such that the n + 1 products
                                               a1 a2 a3 ··· an ,
                                               b 1 a2 a3 ··· an ,
                                               b 1 b 2 a3 ··· an ,
                                                         ..
                                                b1 b2 b 3 ··· bn
form a strictly increasing arithmetic progression in that order. Determine the smallest positive
integer that could be the common difference of such an arithmetic progression.
```

## N5 — Number Theory

```
Let a1 < a2 < a3 < ··· be positive integers such that ak+1 divides 2pa1 + a2 + ··· + ak q
for every k ≥ 1. Suppose that for infinitely many primes p, there exists k such that p divides
ak . Prove that for every positive integer n, there exists k such that n divides ak .
```

## N6 — Number Theory

```
A sequence of integers a0 , a1 , a2 , . . . is called kawaii, if a0 = 0, a1 = 1, and, for any
positive integer n, we have
                           pan+1 − 3an + 2an−1 qpan+1 − 4an + 3an−1 q = 0.
An integer is called kawaii if it belongs to a kawaii sequence.
   Suppose that two consecutive positive integers m and m + 1 are both kawaii (not necessarily
belonging to the same kawaii sequence). Prove that 3 divides m, and that m{3 is kawaii.
```

## N7 — Number Theory

```
Let a, b, c, d be positive integers satisfying
                                  ab      cd     pa + bqpc + dq
                                      +        =                .
                                a+b c+d          a+b+c+d
Determine all possible values of a + b + c + d.
```

## N8 — Number Theory  (Taiwan)

```
Let Z>0 be the set of positive integers. Determine all functions f : Z>0 → Z>0 such
                                       f bf paq pa + 1q = pa + 1qf pbq
holds for all a, b P Z>0 , where f k pnq = f pf p··· f pnq ··· qq denotes the composition of f with
itself k times.
                                                                                              (Taiwan)

10   Chiba, Japan, 2nd–13th July 2023

Shortlisted problems – solutions                                                                 11

                                        Solutions
 A1.       Professor Oak is feeding his 100 Pokémon. Each Pokémon has a bowl whose capacity
is a positive real number of kilograms. These capacities are known to Professor Oak. The total
capacity of all the bowls is 100 kilograms. Professor Oak distributes 100 kilograms of food in
such a way that each Pokémon receives a non-negative integer number of kilograms of food
(which may be larger than the capacity of their bowl). The dissatisfaction level of a Pokémon
who received N kilograms of food and whose bowl has a capacity of C kilograms is equal to
|N − C|.
    Find the smallest real number D such that, regardless of the capacities of the bowls, Pro-
fessor Oak can distribute the food in a way that the sum of the dissatisfaction levels over all
the 100 Pokémon is at most D.
Answer: The answer is D = 50.
```
