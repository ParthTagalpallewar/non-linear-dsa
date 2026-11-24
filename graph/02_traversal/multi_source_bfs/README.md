# Multi-Source BFS

**P1**

## 1. What is the algorithm?

Multi-source BFS starts several vertices in the queue at distance zero.

## 2. Problem it solves

Find the nearest of several exits, facilities, or initial infection points.

## 3. Core intuition

All sources share the same initial layer, so their waves compete in one queue.

## 4. Prerequisites

Single-source BFS and unit edge costs.

## 5. How it works

1. Assign distance zero to all sources.
2. Enqueue the distinct sources.
3. Assign each first-seen neighbor its predecessor's distance plus one.

## 6. Visual example

```text
0 → 1 → 2 ← 3
```

## 7. Dry run

Queue [0, 3] grows to [3, 1], then [1, 2]. Both 1 and 2 get distance 1.

## 8. Python implementation

Start with `multi_source_bfs` in [implementation.py](implementation.py). Assign each first-seen neighbor its predecessor's distance plus one.

## 9. Time and space complexity

For S source entries, V reached vertices and E inspected edges, time is O(S + V + E) and space is O(V), including the distance result.

## 10. Why the algorithm works

A shorter path would have a predecessor in an earlier layer, which would already have discovered the vertex.

## 11. When to use it

Find the nearest of several exits, facilities, or initial infection points.

## 12. When not to use it

Use a weighted shortest-path algorithm for nonuniform costs.

## 13. Common mistakes

Seed and deduplicate every source before expanding any edges.

## 14. Alternative approaches

Running BFS from each source separately can cost O(S(V + E)).

## 15. Practice problems

**Original exercise · P1.** Compute a grid's distance to the nearest zero from every cell.

## 16. Interview revision notes

All sources share the same initial layer, so their waves compete in one queue. Seed and deduplicate every source before expanding any edges.
