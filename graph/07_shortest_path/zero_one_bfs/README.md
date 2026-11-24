# 0–1 BFS

**P2**

## 1. What is the algorithm?

Find shortest routes when a move is free or costs one.

## 2. Problem it solves

Find shortest routes when a move is free or costs one.

## 3. Core intuition

A deque orders tentative distances because an expansion generates only the current distance and the next distance.

## 4. Prerequisites

Adjacency or edge lists, distance arrays, and edge relaxation.

## 5. How it works

1. Put the source in the deque.
2. Skip stale entries when popping the front.
3. Push zero-cost improvements to the front and unit-cost improvements to the back.

## 6. Visual example

```text
0 ─1→ 1
 \0→ 2 ─0↗
```

## 7. Dry run

After 0, the deque contains (0, 2) then (1, 1). Expanding 2 inserts (0, 1) at the front and makes (1, 1) stale.

## 8. Python implementation

Start with `zero_one_bfs` in [implementation.py](implementation.py). Push zero-cost improvements to the front and unit-cost improvements to the back.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V vertices and E edges, time is O(V + E) and auxiliary space is O(V + E), including stale deque entries.

## 10. Why the algorithm works

The first current entry for a vertex is globally minimum, as in Dijkstra. Deque insertion maintains that minimum at the front.

## 11. When to use it

Find shortest routes when a move is free or costs one.

## 12. When not to use it

Weights outside zero and one can break deque ordering.

## 13. Common mistakes

A vertex can improve after its first insertion, so test distance rather than first discovery.

## 14. Alternative approaches

Heap Dijkstra supports any nonnegative weight.

## 15. Practice problems

**Original exercise · P2.** Trace the algorithm with a disconnected fourth vertex and explain its final distance.

## 16. Interview revision notes

A deque orders tentative distances because an expansion generates only the current distance and the next distance. A vertex can improve after its first insertion, so test distance rather than first discovery.
