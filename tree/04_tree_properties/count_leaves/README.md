# Count Leaf Nodes

**P1**

## 1. What is the algorithm?

Compute count leaf nodes from child summaries.

## 2. Problem it solves

Compute count leaf nodes from child summaries.

## 3. Core intuition

Count one at each childless node and sum leaves across both children.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle a missing root.
2. Count one at each childless node and sum leaves across both children.
3. Return the finalized measurement or predicate.

## 6. Visual example

```text
    1
   / \
  2   3
 /
4
```

## 7. Dry run

Leaves 4 and 3 each return 1. After visiting node 2 and then the root, the result is 2.

## 8. Python implementation

Start with `count_leaves` in [implementation.py](implementation.py). Return the finalized measurement or predicate.

## 9. Time and space complexity

For N nodes and tree height H, time is O(N) and stack space O(H + 1).

## 10. Why the algorithm works

An internal node is excluded and all its leaves belong to exactly one child subtree.

## 11. When to use it

Compute count leaf nodes from child summaries.

## 12. When not to use it

Inputs must be proper trees without shared children or cycles.

## 13. Common mistakes

Use the documented empty-tree base case to make both leaves and missing children work.

## 14. Alternative approaches

An explicit stack can replace recursive traversal when depth is unbounded.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Count one at each childless node and sum leaves across both children. Use the documented empty-tree base case to make both leaves and missing children work.
