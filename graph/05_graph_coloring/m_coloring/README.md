# M-Coloring Using Backtracking

**P1**

## 1. What is the algorithm?

M-Coloring Using Backtracking answers a structural question about a graph.

## 2. Problem it solves

Find a feasible assignment with a fixed number of labels.

## 3. Core intuition

Try every locally valid color and undo a choice if the remaining graph cannot be colored.

## 4. Prerequisites

Adjacency lists, vertex indexing, and the traversal used by the implementation.

## 5. How it works

1. Initialize per-vertex state.
2. Try every locally valid color and undo a choice if the remaining graph cannot be colored.
3. Use the final state to produce the result.

## 6. Visual example

```text
0 — 1
 \ /
  2
```

## 7. Dry run

For the triangle with two colors, assigning [0, 1, −1] leaves no choice for the last vertex. The search backtracks and exhausts the symmetric choices.

## 8. Python implementation

Start with `m_coloring` in [implementation.py](implementation.py). Use the final state to produce the result.

## 9. Time and space complexity

For V vertices, E edges, and M colors, a loose upper bound is O((V + E)(M + 1)^V) time. Auxiliary space is O(V + E) in the worst case because active frames hold forbidden sets.

## 10. Why the algorithm works

Every partial assignment satisfies all edges among assigned vertices. The search branches over every color consistent with those assignments, so any feasible solution remains reachable.

## 11. When to use it

Find a feasible assignment with a fixed number of labels.

## 12. When not to use it

Large general graphs can make exhaustive search infeasible.

## 13. Common mistakes

Reset the current color after a failed branch. Detect self-loops before trying any color.

## 14. Alternative approaches

For two colors, use a linear-time bipartite check.

## 15. Practice problems

**Original exercise · P1.** Modify the example to include an isolated vertex and predict how the result changes.

## 16. Interview revision notes

Try every locally valid color and undo a choice if the remaining graph cannot be colored. Reset the current color after a failed branch. Detect self-loops before trying any color.
