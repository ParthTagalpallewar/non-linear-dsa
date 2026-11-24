# Bellman–Ford

**P2**

## 1. What is the algorithm?

Find shortest distances in a graph with negative edges and detect reachable negative cycles.

## 2. Problem it solves

Find shortest distances in a graph with negative edges and detect reachable negative cycles.

## 3. Core intuition

Repeated edge scans propagate improvements through paths of increasing length.

## 4. Prerequisites

Adjacency or edge lists, distance arrays, and edge relaxation.

## 5. How it works

1. Initialize only the source at zero.
2. Relax every edge up to V−1 times, stopping when a pass changes nothing.
3. Reject further improvements as evidence of a reachable negative cycle.

## 6. Visual example

```text
0 ─2→ 1 ─(−3)→ 2
```

## 7. Dry run

Scan [(1, 2, −3), (0, 1, 2)] from 0. The first pass gives [0, 2, ∞], and the second gives [0, 2, −1].

## 8. Python implementation

Start with `bellman_ford` in [implementation.py](implementation.py). Reject further improvements as evidence of a reachable negative cycle.

## 9. Time and space complexity

For V vertices and E edges, time is O(VE + V) worst case and O(V + E) when the first pass is stable. Auxiliary space is O(V).

## 10. Why the algorithm works

Without a reachable negative cycle, every optimal route can be made simple and uses at most V−1 edges. Each pass handles at least one more edge of every route.

## 11. When to use it

Find shortest distances in a graph with negative edges and detect reachable negative cycles.

## 12. When not to use it

Use a faster specialized algorithm for a DAG or exclusively nonnegative weights.

## 13. Common mistakes

Only report a negative cycle if it is reachable from the source.

## 14. Alternative approaches

Dijkstra avoids repeated edge scans when weights are nonnegative.

## 15. Practice problems

**Original exercise · P2.** Trace the algorithm with a disconnected fourth vertex and explain its final distance.

## 16. Interview revision notes

Repeated edge scans propagate improvements through paths of increasing length. Only report a negative cycle if it is reachable from the source.
