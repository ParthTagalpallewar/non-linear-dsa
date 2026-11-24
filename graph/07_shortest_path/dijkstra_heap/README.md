# Dijkstra Using a Priority Queue

**P1**

## 1. What is the algorithm?

Compute single-source shortest distances with nonnegative edge costs.

## 2. Problem it solves

Compute single-source shortest distances with nonnegative edge costs.

## 3. Core intuition

The unsettled vertex with smallest tentative distance can be finalized.

## 4. Prerequisites

Adjacency or edge lists, distance arrays, and edge relaxation.

## 5. How it works

1. Initialize tentative distances.
2. Pop the minimum candidate and discard stale heap entries.
3. Relax each outgoing edge of the minimum-distance vertex.

## 6. Visual example

```text
0 ─8→ 1
 \1→ 2 ─2↗
```

## 7. Dry run

From 0 we discover 1 at cost 8 and 2 at cost 1. Selecting 2 first improves 1 to cost 3.

## 8. Python implementation

Start with `dijkstra_heap` in [implementation.py](implementation.py). Relax each outgoing edge of the minimum-distance vertex.

Run the example from the repository root with `uv run python -m graph.07_shortest_path.dijkstra_heap.implementation`.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V vertices and E directed edges, time is O(V + E log(E + 1)) and auxiliary space O(V + E) for the lazy heap.

## 10. Why the algorithm works

Any unexamined alternative must cross to an unsettled vertex whose best possible prefix costs at least the current minimum. Nonnegative suffixes cannot improve that bound.

## 11. When to use it

Compute single-source shortest distances with nonnegative edge costs.

## 12. When not to use it

Negative edges can invalidate finalized distances.

## 13. Common mistakes

Reject negative weights and use strict improvements so zero-weight cycles do not reschedule vertices.

## 14. Alternative approaches

Use the array scan for dense graphs where heap operations can dominate.

## 15. Practice problems

- LeetCode #743, Medium. Single-source nonnegative shortest paths. [Network Delay Time](https://leetcode.com/problems/network-delay-time/)

**Original exercise · P1.** Trace the algorithm with a disconnected fourth vertex and explain its final distance.

## 16. Interview revision notes

The unsettled vertex with smallest tentative distance can be finalized. Reject negative weights and use strict improvements so zero-weight cycles do not reschedule vertices.
