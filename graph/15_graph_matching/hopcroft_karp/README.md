# Hopcroft–Karp Algorithm

**P3**

## 1. What is the algorithm?

Find a maximum cardinality matching in a large bipartite graph.

## 2. Problem it solves

Find a maximum cardinality matching in a large bipartite graph.

## 3. Core intuition

Layer every free left vertex at once and augment along a maximal family of independent shortest alternating paths before rebuilding layers.

## 4. Prerequisites

Graph representations and the traversal or recurrence used below.

## 5. How it works

1. Run a multi-source BFS through alternating edges.
2. Search only along layer-respecting routes to the closest free right vertices.
3. Flip a maximal family of shortest paths and repeat.

## 6. Visual example

```text
L0 ─ R0
 |   /
L1  R1
```

## 7. Dry run

The first phase may assign L0 to R0. The next layer search from L1 goes through R0's partner L0 and exits at R1.

## 8. Python implementation

Start with `hopcroft_karp` in [implementation.py](implementation.py). Flip a maximal family of shortest paths and repeat.

## 9. Time and space complexity

For V total vertices and E edges, the standard bound is O(E√V) after isolating zero-degree vertices. This version scans all left vertices each phase, so its bound is O(V + (V + E)√V). Space is O(V).

## 10. Why the algorithm works

A phase eliminates the current shortest augmenting length. After about √V such phases, remaining independent augmenting paths are long enough that fewer than about √V additional augmentations are possible.

## 11. When to use it

Find a maximum cardinality matching in a large bipartite graph.

## 12. When not to use it

This handles unweighted bipartite matching. The recursive DFS can hit Python's recursion limit on long augmenting paths.

## 13. Common mistakes

Only stop at a free right vertex on the shortest layer, and keep edge cursors to avoid rescans in one phase.

## 14. Alternative approaches

Single-path augmentation has a shorter implementation and is easier to trace on tiny graphs.

## 15. Practice problems

**Original exercise · P3.** Modify the worked example to introduce an isolated vertex, and predict the result before running the code.

## 16. Interview revision notes

Layer every free left vertex at once and augment along a maximal family of independent shortest alternating paths before rebuilding layers. Only stop at a free right vertex on the shortest layer, and keep edge cursors to avoid rescans in one phase.
