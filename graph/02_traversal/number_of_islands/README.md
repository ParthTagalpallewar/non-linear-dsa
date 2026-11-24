# Number of Islands

**P1**

## 1. What is the algorithm?

Number of Islands counts connected components of land in a binary grid.

## 2. Problem it solves

Count separate regions when adjacent land cells belong to the same group.

## 3. Core intuition

Every new land seed accounts for one island. A complete search marks the entire island before the scan continues.

## 4. Prerequisites

Grid indexing, connected components, and depth-first search.

## 5. How it works

1. Scan cells in row-major order.
2. Increment the count for each unseen land seed.
3. Mark every land cell reachable from the seed.

## 6. Visual example

```text
1 1 0
0 0 1
1 0 1
```

## 7. Dry run

The first DFS marks (0, 0) and (0, 1). The second marks (1, 2) and (2, 2). The last marks (2, 0), giving 3.

## 8. Python implementation

Start with `number_of_islands` in [implementation.py](implementation.py). Mark every land cell reachable from the seed.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For R rows and C columns, the worst case is O(RC) time and O(RC) auxiliary space. Each reached cell has at most four neighbors.

## 10. Why the algorithm works

Every island has a first cell in scan order. Its search stays on land and discovers the full component, so later cells in that component cannot increment the count.

## 11. When to use it

Count separate regions when adjacent land cells belong to the same group.

## 12. When not to use it

For repeated queries as land is added, rebuilds repeat work that can be tracked incrementally.

## 13. Common mistakes

Mark a cell when adding it to the stack. Touching at a corner does not connect four-way islands.

## 14. Alternative approaches

Use a queue for equivalent BFS or disjoint sets for incremental land additions.

## 15. Practice problems

- LeetCode #200, Medium. Four-connected component counting. [Number of Islands](https://leetcode.com/problems/number-of-islands/)

**Original exercise · P1.** Return the size of the largest island as part of the same scan.

## 16. Interview revision notes

Every new land seed accounts for one island. A complete search marks the entire island before the scan continues. Mark a cell when adding it to the stack. Touching at a corner does not connect four-way islands.
