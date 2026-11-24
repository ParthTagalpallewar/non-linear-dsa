# Borůvka’s Algorithm

**P3**

## 1. What is the algorithm?

Select minimum-total-weight connecting edges.

## 2. Problem it solves

Connect the vertices of each component as cheaply as possible without keeping cycles.

## 3. Core intuition

Identify a cheapest outgoing edge per current component, then perform all safe merges.

## 4. Prerequisites

Undirected weighted graphs, forests, and the cut property.

## 5. How it works

1. Scan edges against current DSU roots.
2. Keep one minimum outgoing edge per root.
3. Merge the candidates that still join distinct components and start another round.

## 6. Visual example

```text
   4
0 ─── 1
 \8  /1
   2
```

## 7. Dry run

Initially 0 proposes 0—1, while 1 and 2 both propose 1—2. The two distinct merges connect the graph.

## 8. Python implementation

Start with `boruvka` in [implementation.py](implementation.py). Merge the candidates that still join distinct components and start another round.

## 9. Time and space complexity

For V vertices and E edges, there are O(log(V + 1)) rounds, costing O(V + E α(V) log(V + 1)) amortized time and O(V) auxiliary space.

## 10. Why the algorithm works

Every chosen edge is minimum across a component cut at the start of the round. DSU keeps an acyclic subset when choices of equal weight overlap. Every component with an outgoing edge joins at least one other.

## 11. When to use it

Connect the vertices of each component as cheaply as possible without keeping cycles.

## 12. When not to use it

A spanning tree minimizes total edge weight. It does not minimize the route length between arbitrary vertices.

## 13. Common mistakes

Stop on an empty proposal set, since disconnected graphs cannot merge into one component.

## 14. Alternative approaches

Prim grows from vertices, Kruskal sorts edges globally, and Borůvka lets every current component propose an edge per round.

## 15. Practice problems

**Original exercise · P3.** Add an isolated vertex and a negative self-loop to the example. Explain why neither contributes a selected edge.

## 16. Interview revision notes

Identify a cheapest outgoing edge per current component, then perform all safe merges. Stop on an empty proposal set, since disconnected graphs cannot merge into one component.
