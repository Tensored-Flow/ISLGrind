# IMO Shortlist 2009 problems
_fidelity: exact_

## A1 — Algebra  (Czech Republic)

```
Find the largest possible integer k, such that the following statement is true:
Let 2009 arbitrary non-degenerated triangles be given. In every triangle the three sides are
colored, such that one is blue, one is red and one is white. Now, for every color separately, let
us sort the lengths of the sides. We obtain

                        b1 ≤ b2 ≤ . . . ≤ b2009      the lengths of the blue sides,
                        r1 ≤ r2 ≤ . . . ≤ r2009      the lengths of the red sides,
              and       w1 ≤ w2 ≤ . . . ≤ w2009      the lengths of the white sides.

Then there exist k indices j such that we can form a non-degenerated triangle with side lengths
bj , rj , wj .
```

## A2 — Algebra  (Estonia)

```
1 1 1
Let a, b, c be positive real numbers such that     + + = a + b + c. Prove that
                                                  a b c
                           1                1               1         3
                                                                    ≤ .
                      (2a + b + c)    (2b + c + a)    (2c + a + b)   16
```

## A3 — Algebra  (France)

```
Determine all functions f from the set of positive integers into the set of positive integers such
that for all x and y there exists a non degenerated triangle with sides of lengths

                                x,   f (y)   and f (y + f (x) − 1).
```

## A4 — Algebra  (Belarus)

```
Let a, b, c be positive real numbers such that ab + bc + ca ≤ 3abc. Prove that

                                                   √ √           √
          r             r            r
             a2 + b 2     b2 + c 2     c 2 + a2                            √   
                      +            +            +3≤ 2     a+b+ b+c+ c+a .
              a+b          b+c          c+a
```

## A5 — Algebra  (Belarus)

```
Let f be any function that maps the set of real numbers into the set of real numbers. Prove
that there exist real numbers x and y such that

                                     f (x − f (y)) > yf (x) + x.

50th IMO 2009                                    Problem Shortlist                             Algebra
```

## A6 — Algebra  (United States of America)

```
Suppose that s1 , s2 , s3 , . . . is a strictly increasing sequence of positive integers such that the
subsequences

                       ss1 , ss2 , ss3 , . . .      and     ss1 +1 , ss2 +1 , ss3 +1 , . . .

are both arithmetic progressions. Prove that s1 , s2 , s3 , . . . is itself an arithmetic progression.
```

## A7 — Algebra  (Japan)

```
Find all functions f from the set of real numbers into the set of real numbers which satisfy for
all real x, y the identity

                                      f (xf (x + y)) = f (yf (x)) + x2 .

Combinatorics                                 Problem Shortlist                                 50th IMO 2009
```

## C1 — Combinatorics  (New Zealand)

```
Consider 2009 cards, each having one gold side and one black side, lying in parallel on a long
table. Initially all cards show their gold sides. Two players, standing by the same long side of
the table, play a game with alternating moves. Each move consists of choosing a block of 50
consecutive cards, the leftmost of which is showing gold, and turning them all over, so those
which showed gold now show black and vice versa. The last player who can make a legal move
wins.
(a) Does the game necessarily end?
(b) Does there exist a winning strategy for the starting player?
```

## C2 — Combinatorics  (Romania)

```
For any integer n ≥ 2, let N (n) be the maximal number of triples (ai , bi , ci ), i = 1, . . . , N (n),
consisting of nonnegative integers ai , bi and ci such that the following two conditions are satis-
fied:
(1) ai + bi + ci = n for all i = 1, . . . , N (n),
(2) If i 6= j, then ai 6= aj , bi 6= bj and ci 6= cj .
Determine N (n) for all n ≥ 2.

Comment. The original problem was formulated for m-tuples instead for triples. The numbers
N (m, n) are then defined similarly to N (n) in the case m = 3. The numbers N (3, n) and
N (n, n) should be determined. The case m = 3 is the same as in the present problem. The
upper bound for N (n, n) can be proved by a simple generalization. The construction of a set
of triples attaining the bound can be easily done by induction from n to n + 2.
```

## C3 — Combinatorics  (Russian Federation)

```
Let n be a positive integer. Given a sequence ε1 , . . . , εn−1 with εi = 0 or εi = 1 for each
i = 1, . . . , n − 1, the sequences a0 , . . . , an and b0 , . . . , bn are constructed by the following rules:

                                        a0 = b0 = 1,     a1 = b1 = 7,

                          2ai−1 + 3ai ,         if εi = 0,
                  ai+1 =                                       for each i = 1, . . . , n − 1,
                          3ai−1 + ai ,          if εi = 1,
                          2bi−1 + 3bi ,         if εn−i = 0,
                  bi+1 =                                       for each i = 1, . . . , n − 1.
                          3bi−1 + bi ,          if εn−i = 1,

Prove that an = bn .
```

## C4 — Combinatorics  (Netherlands)

```
For an integer m ≥ 1, we consider partitions of a 2m × 2m chessboard into rectangles consisting
of cells of the chessboard, in which each of the 2m cells along one diagonal forms a separate
rectangle of side length 1. Determine the smallest possible sum of rectangle perimeters in such
a partition.

50th IMO 2009                              Problem Shortlist                              Combinatorics
```

## C5 — Combinatorics  (Netherlands)

```
Five identical empty buckets of 2-liter capacity stand at the vertices of a regular pentagon.
Cinderella and her wicked Stepmother go through a sequence of rounds: At the beginning of
every round, the Stepmother takes one liter of water from the nearby river and distributes it
arbitrarily over the five buckets. Then Cinderella chooses a pair of neighboring buckets, empties
them into the river, and puts them back. Then the next round begins. The Stepmother’s goal
is to make one of these buckets overflow. Cinderella’s goal is to prevent this. Can the wicked
Stepmother enforce a bucket overflow?
```

## C6 — Combinatorics  (Bulgaria)

```
On a 999 × 999 board a limp rook can move in the following way: From any square it can move
to any of its adjacent squares, i.e. a square having a common side with it, and every move
must be a turn, i.e. the directions of any two consecutive moves must be perpendicular. A non-
intersecting route of the limp rook consists of a sequence of pairwise different squares that the
limp rook can visit in that order by an admissible sequence of moves. Such a non-intersecting
route is called cyclic, if the limp rook can, after reaching the last square of the route, move
directly to the first square of the route and start over.
How many squares does the longest possible cyclic, non-intersecting route of a limp rook
visit?
```

## C7 — Combinatorics  (Russian Federation)

```
Variant 1. A grasshopper jumps along the real axis. He starts at point 0 and makes 2009
jumps to the right with lengths 1, 2, . . . , 2009 in an arbitrary order. Let M be a set of 2008
positive integers less than 1005 · 2009. Prove that the grasshopper can arrange his jumps in
such a way that he never lands on a point from M .

Variant 2. Let n be a nonnegative integer. A grasshopper jumps along the real axis. He starts
at point 0 and makes n + 1 jumps to the right with pairwise different positive integral lengths
a1 , a2 , . . . , an+1 in an arbitrary order. Let M be a set of n positive integers in the interval (0, s),
where s = a1 + a2 + · · · + an+1 . Prove that the grasshopper can arrange his jumps in such a
way that he never lands on a point from M .
```

## C8 — Combinatorics  (Austria)

```
For any integer n ≥ 2, we compute the integer h(n) by applying the following procedure to its
decimal representation. Let r be the rightmost digit of n.
(1) If r = 0, then the decimal representation of h(n) results from the decimal representation
    of n by removing this rightmost digit 0.
(2) If 1 ≤ r ≤ 9 we split the decimal representation of n into a maximal right part R that
    solely consists of digits not less than r and into a left part L that either is empty or ends
    with a digit strictly smaller than r. Then the decimal representation of h(n) consists of the
    decimal representation of L, followed by two copies of the decimal representation of R − 1.
    For instance, for the number n = 17,151,345,543, we will have L = 17,151, R = 345,543
    and h(n) = 17,151,345,542,345,542.
Prove that, starting with an arbitrary integer n ≥ 2, iterated application of h produces the
integer 1 after finitely many steps.

Geometry                               Problem Shortlist                     50th IMO 2009
```

## G1 — Geometry  (Belgium)

```
Let ABC be a triangle with AB = AC. The angle bisectors of A and B meet the sides BC
and AC in D and E, respectively. Let K be the incenter of triangle ADC. Suppose that
∠BEK = 45 ◦. Find all possible values of ∠BAC.
```

## G2 — Geometry  (Russian Federation)

```
Let ABC be a triangle with circumcenter O. The points P and Q are interior points of the
sides CA and AB, respectively. The circle k passes through the midpoints of the segments BP ,
CQ, and P Q. Prove that if the line P Q is tangent to circle k then OP = OQ.
```

## G3 — Geometry  (Islamic Republic of Iran)

```
Let ABC be a triangle. The incircle of ABC touches the sides AB and AC at the points Z
and Y , respectively. Let G be the point where the lines BY and CZ meet, and let R and S be
points such that the two quadrilaterals BCY R and BCSZ are parallelograms.
Prove that GR = GS.
```

## G4 — Geometry  (United Kingdom)

```
Given a cyclic quadrilateral ABCD, let the diagonals AC and BD meet at E and the lines AD
and BC meet at F . The midpoints of AB and CD are G and H, respectively. Show that EF
is tangent at E to the circle through the points E, G, and H.
```

## G5 — Geometry  (Poland)

```
Let P be a polygon that is convex and symmetric to some point O. Prove that for some
parallelogram R satisfying P ⊂ R we have

                                           |R| √
                                                ≤ 2

where |R| and |P | denote the area of the sets R and P , respectively.
```

## G6 — Geometry  (Ukraine)

```
Let the sides AD and BC of the quadrilateral ABCD (such that AB is not parallel to CD)
intersect at point P . Points O1 and O2 are the circumcenters and points H1 and H2 are the
orthocenters of triangles ABP and DCP , respectively. Denote the midpoints of segments
O1 H1 and O2 H2 by E1 and E2 , respectively. Prove that the perpendicular from E1 on CD, the
perpendicular from E2 on AB and the line H1 H2 are concurrent.
```

## G7 — Geometry  (Islamic Republic of Iran)

```
Let ABC be a triangle with incenter I and let X, Y and Z be the incenters of the triangles
BIC, CIA and AIB, respectively. Let the triangle XY Z be equilateral. Prove that ABC is
equilateral too.

50th IMO 2009                       Problem Shortlist                          Geometry
```

## G8 — Geometry  (Bulgaria)

```
Let ABCD be a circumscribed quadrilateral. Let g be a line through A which meets the
segment BC in M and the line CD in N . Denote by I1 , I2 , and I3 the incenters of 4ABM ,
4M N C, and 4N DA, respectively. Show that the orthocenter of 4I1 I2 I3 lies on g.

Number Theory                             Problem Shortlist                            50th IMO 2009
```

## N1 — Number Theory  (Australia)

```
A social club has n members. They have the membership numbers 1, 2, . . . , n, respectively.
From time to time members send presents to other members, including items they have already
received as presents from other members. In order to avoid the embarrassing situation that a
member might receive a present that he or she has sent to other members, the club adds the
following rule to its statutes at one of its annual general meetings:
“A member with membership number a is permitted to send a present to a member with
membership number b if and only if a(b − 1) is a multiple of n.”
Prove that, if each member follows this rule, none will receive a present from another member
that he or she has already sent to other members.

Alternative formulation: Let G be a directed graph with n vertices v1 , v2 , . . . , vn , such that
there is an edge going from va to vb if and only if a and b are distinct and a(b − 1) is a multiple
of n. Prove that this graph does not contain a directed cycle.
```

## N2 — Number Theory  (Peru)

```
A positive integer N is called balanced, if N = 1 or if N can be written as a product of an
even number of not necessarily distinct primes. Given positive integers a and b, consider the
polynomial P defined by P (x) = (x + a)(x + b).
 (a) Prove that there exist distinct positive integers a and b such that all the numbers P (1), P (2),
     . . . , P (50) are balanced.
 (b) Prove that if P (n) is balanced for all positive integers n, then a = b.
```

## N3 — Number Theory  (Estonia)

```
Let f be a non-constant function from the set of positive integers into the set of positive integers,
such that a − b divides f (a) − f (b) for all distinct positive integers a, b. Prove that there exist
infinitely many primes p such that p divides f (c) for some positive integer c.
```

## N4 — Number Theory

```
Find all positive integers n such that there exists a sequence of positive integers a1 , a2 , . . . , an
satisfying
                                               a2 + 1
                                      ak+1 = k         −1
                                              ak−1 + 1
for every k with 2 ≤ k ≤ n − 1.
```

## N5 — Number Theory  (Hungary)

```
Let P (x) be a non-constant polynomial with integer coefficients. Prove that there is no function
T from the set of integers into the set of integers such that the number of integers x with
T n (x) = x is equal to P (n) for every n ≥ 1, where T n denotes the n-fold application of T .

50th IMO 2009                             Problem Shortlist                           Number Theory
```

## N6 — Number Theory  (Turkey)

```
Let k be a positive integer. Show that if there exists a sequence a0 , a1 , . . . of integers satisfying
the condition
                                          an−1 + nk
                                   an =               for all n ≥ 1,
then k − 2 is divisible by 3.
```

## N7 — Number Theory  (Mongolia)

```
Let a and b be distinct integers greater than 1. Prove that there exists a positive integer n such
that (an − 1)(bn − 1) is not a perfect square.

A1                                             Algebra                                 50th IMO 2009

A1         CZE      (Czech Republic)
Find the largest possible integer k, such that the following statement is true:
Let 2009 arbitrary non-degenerated triangles be given. In every triangle the three sides are
colored, such that one is blue, one is red and one is white. Now, for every color separately, let
us sort the lengths of the sides. We obtain

                          b1 ≤ b2 ≤ . . . ≤ b2009      the lengths of the blue sides,
                          r1 ≤ r2 ≤ . . . ≤ r2009      the lengths of the red sides,
               and        w1 ≤ w2 ≤ . . . ≤ w2009      the lengths of the white sides.

Then there exist k indices j such that we can form a non-degenerated triangle with side lengths
bj , rj , wj .
```
