# Heavy-Light Decomposition

**P3**

## 1. What is the algorithm?

Answer arbitrary path sums even when individual vertex values change.

## 2. Problem it solves

Answer arbitrary path sums even when individual vertex values change.

## 3. Core intuition

Make each largest-child chain contiguous. Every time a path leaves a chain upward, it crosses an edge to a subtree at least twice the size.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Root the tree and compute subtree sizes.
2. Number the heaviest child before scheduling the remaining children.
3. Climb from the deeper chain head, summing each contiguous segment before the final shared chain.

## 6. Visual example

```text
    0
   / \
  1   2
 / \
3   4
```

## 7. Dry run

For path 4→2, 4 can be a separate chain. Sum its slot, jump to 1, then handle the chain for 2 and the final shared segment through 0.

## 8. Python implementation

Start with `heavy_light_decomposition` in [implementation.py](implementation.py). Climb from the deeper chain head, summing each contiguous segment before the final shared chain.

## 9. Time and space complexity

For N vertices, preprocessing and storage are O(N), point assignments O(log(N + 1)), and path sums O(log²(N + 1)) with O(1) per-query auxiliary space.

## 10. Why the algorithm works

A light child occupies at most half its parent's subtree. Each endpoint therefore crosses only logarithmically many chain boundaries. Visited segments partition the path.

## 11. When to use it

Answer arbitrary path sums even when individual vertex values change.

## 12. When not to use it

Use these routines on undirected trees with symmetric adjacency and integer IDs 0 through N−1.

## 13. Common mistakes

When heads differ, climb from the deeper head. The final shared segment includes the LCA exactly once.

## 14. Alternative approaches

Use static root prefixes and LCA when values never change, or swap the Fenwick index for a segment tree to support min/max.

## 15. Practice problems

**Original exercise · P3.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Make each largest-child chain contiguous. Every time a path leaves a chain upward, it crosses an edge to a subtree at least twice the size. When heads differ, climb from the deeper head. The final shared segment includes the LCA exactly once.
