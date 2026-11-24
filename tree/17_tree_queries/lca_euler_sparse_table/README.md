# LCA Using Euler Tour and Sparse Table

**P3**

## 1. What is the algorithm?

Answer a static LCA query using two precomputed range-minimum blocks.

## 2. Problem it solves

Answer a static LCA query using two precomputed range-minimum blocks.

## 3. Core intuition

The shallowest visit between the endpoints' first Euler occurrences is their common ancestor.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Root the undirected tree and preprocess the indicated index.
2. The shallowest visit between the endpoints' first Euler occurrences is their common ancestor.
3. Return the result for each requested vertex or pair.

## 6. Visual example

```text
    0
   / \
  1   2
 / \
3   4
```

## 7. Dry run

In walk [0, 1, 3, 1, 4, 1, 0, 2, 0], first positions 2 and 4 span [3, 1, 4]. Minimum depth belongs to 1.

## 8. Python implementation

Start with `lca_euler_sparse_table` in [implementation.py](implementation.py). Return the result for each requested vertex or pair.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes, build time and storage O(N log(N + 1)), with O(1) time and space per query.

## 10. Why the algorithm works

The tour must ascend to the LCA before entering the second endpoint's branch but cannot ascend higher before that endpoint is reached. Overlapping sparse-table blocks are valid because minimum is idempotent.

## 11. When to use it

Answer a static LCA query using two precomputed range-minimum blocks.

## 12. When not to use it

The index assumes a fixed tree structure. Rebuild it after edges change.

## 13. Common mistakes

Compare depth rather than vertex ID and use the inclusive interval between first visits.

## 14. Alternative approaches

For very few queries, traverse the tree directly.

## 15. Practice problems

**Original exercise · P3.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

The shallowest visit between the endpoints' first Euler occurrences is their common ancestor. Compare depth rather than vertex ID and use the inclusive interval between first visits.
