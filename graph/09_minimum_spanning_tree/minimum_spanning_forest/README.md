# Minimum Spanning Forest

**P2**

## 1. What is the algorithm?

Select minimum-total-weight connecting edges.

## 2. Problem it solves

Connect the vertices of each component as cheaply as possible without keeping cycles.

## 3. Core intuition

Kruskal accepts a safe edge wherever it appears, so each separate component is spanned independently.

## 4. Prerequisites

Undirected weighted graphs, forests, and the cut property.

## 5. How it works

1. Initialize every vertex as an isolated tree.
2. Scan the edges in increasing weight.
3. Keep each edge that joins two different partial trees and retain all isolated vertices through the vertex count.

## 6. Visual example

```text
   4
0 ─── 1
 \8  /1
   2
```

## 7. Dry run

The triangle produces its two cheapest connecting edges. A fourth isolated vertex contributes zero edges.

## 8. Python implementation

Start with `minimum_spanning_forest` in [implementation.py](implementation.py). Keep each edge that joins two different partial trees and retain all isolated vertices through the vertex count.

## 9. Time and space complexity

For V vertices and E edges, time is O(V + E log(E + 1)) and auxiliary space O(V + E) with a sorted edge copy.

## 10. Why the algorithm works

Within any original component the accepted edges cannot form a cycle. If two groups in a component were still disconnected, an input edge between groups would have merged them when scanned.

## 11. When to use it

Connect the vertices of each component as cheaply as possible without keeping cycles.

## 12. When not to use it

A spanning tree minimizes total edge weight. It does not minimize the route length between arbitrary vertices.

## 13. Common mistakes

A graph with C connected components contributes V−C selected edges, including zero edges for singleton trees.

## 14. Alternative approaches

Prim grows from vertices, Kruskal sorts edges globally, and Borůvka lets every current component propose an edge per round.

## 15. Practice problems

**Original exercise · P2.** Add an isolated vertex and a negative self-loop to the example. Explain why neither contributes a selected edge.

## 16. Interview revision notes

Kruskal accepts a safe edge wherever it appears, so each separate component is spanned independently. A graph with C connected components contributes V−C selected edges, including zero edges for singleton trees.
