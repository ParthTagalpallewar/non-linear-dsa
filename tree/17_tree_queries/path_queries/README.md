# Static Path Sum Queries

**P2**

## 1. What is the algorithm?

Sum all values along a path between arbitrary vertex pairs.

## 2. Problem it solves

Sum all values along a path between arbitrary vertex pairs.

## 3. Core intuition

Combine two root prefixes and remove their shared initial segment, adding the LCA once.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Root the undirected tree and preprocess the indicated index.
2. Combine two root prefixes and remove their shared initial segment, adding the LCA once.
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

For values [8, 2, −5, 4, 1], the path 3→1→0→2 sums to 4 + 2 + 8 − 5 = 9.

## 8. Python implementation

Start with `path_queries` in [implementation.py](implementation.py). Return the result for each requested vertex or pair.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes and Q queries, total time O((N + Q) log(N + 1)), index storage O(N log(N + 1)), and output O(Q).

## 10. Why the algorithm works

The root paths overlap precisely through their LCA. Subtracting its entire prefix twice cancels both copies, so adding its value restores it once.

## 11. When to use it

Sum all values along a path between arbitrary vertex pairs.

## 12. When not to use it

The index assumes a fixed tree structure. Rebuild it after edges change.

## 13. Common mistakes

The formula differs for edge-weight sums, which do not add an LCA node value.

## 14. Alternative approaches

Heavy-light decomposition supports path queries when values change.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Combine two root prefixes and remove their shared initial segment, adding the LCA once. The formula differs for edge-weight sums, which do not add an LCA node value.
