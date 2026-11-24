# Kruskal’s Algorithm

**P1**

## 1. What is the algorithm?

Select minimum-total-weight connecting edges.

## 2. Problem it solves

Connect the vertices of each component as cheaply as possible without keeping cycles.

## 3. Core intuition

Process edges in global weight order and join only distinct components.

## 4. Prerequisites

Undirected weighted graphs, forests, and the cut property.

## 5. How it works

1. Sort edges by weight.
2. Use DSU to check whether endpoints are already connected.
3. Append every edge that merges two components.

## 6. Visual example

```text
   4
0 ─── 1
 \8  /1
   2
```

## 7. Dry run

Process 1—2 at weight 1, then 0—1 at weight 4. The weight-8 edge 0—2 is rejected.

## 8. Python implementation

Start with `kruskal` in [implementation.py](implementation.py). Append every edge that merges two components.

## 9. Time and space complexity

For V vertices and E edges, time is O(V + E log(E + 1)) and auxiliary space O(V + E), including the sorted copy.

## 10. Why the algorithm works

Each accepted edge is a minimum-weight crossing edge for its current component. The cut property guarantees that such an edge can extend an optimal forest.

## 11. When to use it

Connect the vertices of each component as cheaply as possible without keeping cycles.

## 12. When not to use it

A spanning tree minimizes total edge weight. It does not minimize the route length between arbitrary vertices.

## 13. Common mistakes

Sort by edge weight and preserve DSU state between edges.

## 14. Alternative approaches

Prim grows from vertices, Kruskal sorts edges globally, and Borůvka lets every current component propose an edge per round.

## 15. Practice problems

**Original exercise · P1.** Add an isolated vertex and a negative self-loop to the example. Explain why neither contributes a selected edge.

## 16. Interview revision notes

Process edges in global weight order and join only distinct components. Sort by edge weight and preserve DSU state between edges.
