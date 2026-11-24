# Prim’s Algorithm Using a Priority Queue

**P2**

## 1. What is the algorithm?

Select minimum-total-weight connecting edges.

## 2. Problem it solves

Connect the vertices of each component as cheaply as possible without keeping cycles.

## 3. Core intuition

Grow one tree at a time by choosing the cheapest edge that crosses from the tree to a new vertex.

## 4. Prerequisites

Undirected weighted graphs, forests, and the cut property.

## 5. How it works

1. Build weighted adjacency lists.
2. Pop the cheapest candidate and discard it if its target already belongs to the forest.
3. Include the chosen edge and record candidates from the new vertex.

## 6. Visual example

```text
   4
0 ─── 1
 \8  /1
   2
```

## 7. Dry run

Starting from 0, choose 0—1 at weight 4. The cheapest crossing edge is now 1—2 at weight 1. The forest weight is 5.

## 8. Python implementation

Start with `prim_heap` in [implementation.py](implementation.py). Include the chosen edge and record candidates from the new vertex.

## 9. Time and space complexity

For V vertices and E edges, time is O(V + E log(E + 1)) and space O(V + E), including adjacency and heap.

## 10. Why the algorithm works

For the cut between the current tree and the remaining vertices, a cheapest crossing edge is safe. Any spanning tree omitting it can exchange an edge across the same cut without increasing cost.

## 11. When to use it

Connect the vertices of each component as cheaply as possible without keeping cycles.

## 12. When not to use it

A spanning tree minimizes total edge weight. It does not minimize the route length between arbitrary vertices.

## 13. Common mistakes

The key is one edge's weight rather than cumulative distance.

## 14. Alternative approaches

Prim grows from vertices, Kruskal sorts edges globally, and Borůvka lets every current component propose an edge per round.

## 15. Practice problems

**Original exercise · P2.** Add an isolated vertex and a negative self-loop to the example. Explain why neither contributes a selected edge.

## 16. Interview revision notes

Grow one tree at a time by choosing the cheapest edge that crosses from the tree to a new vertex. The key is one edge's weight rather than cumulative distance.
