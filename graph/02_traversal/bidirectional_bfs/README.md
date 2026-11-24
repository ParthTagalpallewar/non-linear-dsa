# Bidirectional BFS

**P2**

## 1. What is the algorithm?

Bidirectional BFS expands BFS layers from both ends until they meet.

## 2. Problem it solves

Find one unweighted source-to-target distance when exploring from both ends is feasible.

## 3. Core intuition

Two shallower searches can visit fewer states than one deep search.

## 4. Prerequisites

BFS layers and an undirected neighbor relation.

## 5. How it works

1. Start independent visited-distance maps.
2. Choose the smaller of the two current frontiers.
3. Expand one layer and return the sum of both distances plus the crossing edge.

## 6. Visual example

```text
0 — 1 — 3 — 4
 \— 2
```

## 7. Dry run

Expand 0 to {1, 2}, then 4 to {3}. Expanding 3 meets 1 and returns 1 + 1 + 1 = 3.

## 8. Python implementation

Start with `bidirectional_bfs` in [implementation.py](implementation.py). Expand one layer and return the sum of both distances plus the crossing edge.

## 9. Time and space complexity

Worst case O(V + E) time and O(V) space for V vertices and E edges. With regular branching b and shortest distance d, two balanced searches can explore about O(b^(d/2)) states.

## 10. Why the algorithm works

Before the first meeting the explored balls are disjoint. Expanding a full-distance layer increases their combined reach by one, so the first intersection gives the shortest length.

## 11. When to use it

Find one unweighted source-to-target distance when exploring from both ends is feasible.

## 12. When not to use it

A single BFS is more useful for distances from one source to every vertex.

## 13. Common mistakes

Expand complete layers. A directed version needs reverse edges on the target side.

## 14. Alternative approaches

Use ordinary BFS when reverse expansion is expensive or unavailable.

## 15. Practice problems

**Original exercise · P2.** Add predecessor maps and reconstruct the route through the meeting edge.

## 16. Interview revision notes

Two shallower searches can visit fewer states than one deep search. Expand complete layers. A directed version needs reverse edges on the target side.
