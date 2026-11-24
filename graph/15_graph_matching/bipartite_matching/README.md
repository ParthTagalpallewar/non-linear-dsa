# Bipartite Matching Using Augmenting Paths

**P2**

## 1. What is the algorithm?

Choose the largest collection of disjoint compatible pairs.

## 2. Problem it solves

Choose the largest collection of disjoint compatible pairs.

## 3. Core intuition

A new left vertex can displace a matched partner if the displaced partner can move to another right vertex.

## 4. Prerequisites

Graph representations and the traversal or recurrence used below.

## 5. How it works

1. Start with all right vertices free.
2. Search for an alternating route from each new left vertex to a free right vertex.
3. Reassign each pair while unwinding a successful search.

## 6. Visual example

```text
L0 ─ R0
 |   /
L1  R1
```

## 7. Dry run

L0 takes R0 first. Searching from L1 moves L0 to R1 and leaves R0 available for L1.

## 8. Python implementation

Start with `bipartite_matching` in [implementation.py](implementation.py). Reassign each pair while unwinding a successful search.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For L left vertices, R right vertices, E edges and M matched pairs, time is O(L(E + 1) + R + M log(M + 1)) and space O(L + R).

## 10. Why the algorithm works

An alternating route to a spare right vertex adds one more unmatched edge than it removes matched edges. If the prefix matching was maximum, any improvement after adding a left vertex must use that vertex.

## 11. When to use it

Choose the largest collection of disjoint compatible pairs.

## 12. When not to use it

Edge costs require weighted assignment. Very long alternating paths can hit Python's recursion limit.

## 13. Common mistakes

Reset the right-side visited set per search, and allow reassignments before giving up.

## 14. Alternative approaches

Hopcroft–Karp searches for multiple shortest augmenting paths per phase.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example to introduce an isolated vertex, and predict the result before running the code.

## 16. Interview revision notes

A new left vertex can displace a matched partner if the displaced partner can move to another right vertex. Reset the right-side visited set per search, and allow reassignments before giving up.
