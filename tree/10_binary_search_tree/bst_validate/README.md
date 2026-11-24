# BST Validation

**P1**

## 1. What is the algorithm?

Determine whether a binary tree satisfies global strict search ordering.

## 2. Problem it solves

Determine whether a binary tree satisfies global strict search ordering.

## 3. Core intuition

Carry the tightest lower and upper bounds accumulated on the root-to-node path.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Initialize the search or traversal at the root.
2. Carry the tightest lower and upper bounds accumulated on the root-to-node path.
3. Return the selected value or updated result.

## 6. Visual example

```text
    4
   / \
  2   6
 / \   \
1   3   8
```

## 7. Dry run

A right child of node 2 in the left subtree of root 4 must lie strictly between 2 and 4.

## 8. Python implementation

Start with `bst_validate` in [implementation.py](implementation.py). Return the selected value or updated result.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes and height H, worst-case time O(N) and auxiliary space O(H + 1).

## 10. Why the algorithm works

All ancestor constraints reduce to an open interval. Passing every interval check is equivalent to strict BST ordering.

## 11. When to use it

Determine whether a binary tree satisfies global strict search ordering.

## 12. When not to use it

For a BST that permits duplicate keys, use its precise side and bound policy.

## 13. Common mistakes

Checking only immediate child values misses deep violations.

## 14. Alternative approaches

A strict BST has strictly increasing inorder output, so a single previous key can also validate it.

## 15. Practice problems

- LeetCode #98, Medium. Strict ancestor bounds. [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Carry the tightest lower and upper bounds accumulated on the root-to-node path. Checking only immediate child values misses deep violations.
