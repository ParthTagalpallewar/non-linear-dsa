# Connected Components Using DFS

**P1**

## 1. What is the algorithm?

Partition an undirected graph into maximal connected groups.

## 2. Problem it solves

Count isolated clusters or group accounts connected through shared identifiers.

## 3. Core intuition

The stack explores the full reachable region before the outer loop chooses another seed.

## 4. Prerequisites

Undirected adjacency lists and transitive connectivity.

## 5. How it works

1. Scan for the next unseen seed.
2. Use a stack to traverse its neighbors and mark on discovery.
3. Save the visited group and resume scanning seeds.

## 6. Visual example

```text
0 — 1    2
```

## 7. Dry run

The stack starts with [0]. Processing 0 adds 1. The next unseen seed is 2.

## 8. Python implementation

Start with `components_dfs` in [implementation.py](implementation.py). Save the visited group and resume scanning seeds.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V vertices and E undirected edges, time is O(V + E) and auxiliary space is O(V). Each adjacency entry is scanned once.

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

The stack explores the full reachable region before the outer loop chooses another seed. Include isolated vertices and inspect every possible seed.
