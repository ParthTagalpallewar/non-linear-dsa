# Height of a Binary Tree

**P1**

## 1. What is the algorithm?

Compute height of a binary tree from child summaries.

## 2. Problem it solves

Compute height of a binary tree from child summaries.

## 3. Core intuition

Use the largest child height plus one to count edges to the deepest leaf.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle a missing root.
2. Use the largest child height plus one to count edges to the deepest leaf.
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

Leaves 4 and 3 each return 0. After visiting node 2 and then the root, the result is 2.

## 8. Python implementation

Start with `height` in [implementation.py](implementation.py). Return the finalized measurement or predicate.

## 9. Time and space complexity

For N nodes and tree height H, time is O(N) and stack space O(H + 1).

## 10. Why the algorithm works

Every longest downward path from an internal node takes exactly one initial child edge and then a longest child path.

## 11. When to use it

Compute height of a binary tree from child summaries.

## 12. When not to use it

Inputs must be proper trees without shared children or cycles.

## 13. Common mistakes

Use the documented empty-tree base case to make both leaves and missing children work.

## 14. Alternative approaches

An explicit stack can replace recursive traversal when depth is unbounded.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Use the largest child height plus one to count edges to the deepest leaf. Use the documented empty-tree base case to make both leaves and missing children work.
