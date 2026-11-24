# Dijkstra Using an Array

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
2. Scan for the unsettled vertex with minimum distance and stop if it is unreachable.
3. Relax each outgoing edge of the minimum-distance vertex.

## 6. Visual example

```text
0 ─8→ 1
 \1→ 2 ─2↗
```

## 7. Dry run

From 0 we discover 1 at cost 8 and 2 at cost 1. Selecting 2 first improves 1 to cost 3.

## 8. Python implementation

Start with `dijkstra_array` in [implementation.py](implementation.py). Relax each outgoing edge of the minimum-distance vertex.

## 9. Time and space complexity

For V vertices and E directed edges, time is O(V² + E), with O(V) auxiliary space. Each minimum selection scans the vertex array.

## 10. Why the algorithm works

Any unexamined alternative must cross to an unsettled vertex whose best possible prefix costs at least the current minimum. Nonnegative suffixes cannot improve that bound.

## 11. When to use it

Compute single-source shortest distances with nonnegative edge costs.

## 12. When not to use it

Negative edges can invalidate finalized distances.

## 13. Common mistakes

Reject negative weights and use strict improvements so zero-weight cycles do not reschedule vertices.

## 14. Alternative approaches

Use a heap to avoid scanning all vertices on sparse graphs.

## 15. Practice problems

**Original exercise · P1.** Trace the algorithm with a disconnected fourth vertex and explain its final distance.

## 16. Interview revision notes

The unsettled vertex with smallest tentative distance can be finalized. Reject negative weights and use strict improvements so zero-weight cycles do not reschedule vertices.
