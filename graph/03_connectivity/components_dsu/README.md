# Connected Components Using DSU

**P1**

## 1. What is the algorithm?

Partition an undirected graph into maximal connected groups.

## 2. Problem it solves

Count isolated clusters or group accounts connected through shared identifiers.

## 3. Core intuition

Each edge establishes that its endpoints belong to the same group, so transitivity lets us merge whole groups.

## 4. Prerequisites

Undirected adjacency lists and transitive connectivity.

## 5. How it works

1. Create a singleton set for each vertex.
2. Merge the endpoints of every edge.
3. Group vertices by their final representative.

## 6. Visual example

```text
0 — 1    2
```

## 7. Dry run

The edge 0—1 merges those two singleton sets. No edge touches 2, so it remains a singleton.

## 8. Python implementation

Start with `components_dsu` in [implementation.py](implementation.py). Group vertices by their final representative.

## 9. Time and space complexity

With V vertices and E edges, time is O((V + E) α(V)) amortized and auxiliary space is O(V). The inverse Ackermann function α grows extremely slowly.

## 10. Why the algorithm works

Vertices joined by an edge must be in the same group. Following any path therefore keeps its endpoints in one group. Every group is built exclusively from existing edges.

## 11. When to use it

Count isolated clusters or group accounts connected through shared identifiers.

## 12. When not to use it

Directed mutual reachability requires strongly connected components.

## 13. Common mistakes

Include isolated vertices and inspect every possible seed.

## 14. Alternative approaches

Traversal is linear on a fixed graph. DSU supports incremental edge additions without repeating a traversal.

## 15. Practice problems

**Original exercise · P1.** Return the size of the largest component.

## 16. Interview revision notes

Each edge establishes that its endpoints belong to the same group, so transitivity lets us merge whole groups. Include isolated vertices and inspect every possible seed.
