# Construct a Full Binary Tree from Preorder and Postorder

**P2**

## 1. What is the algorithm?

Reconstruct a tree uniquely when preorder and postorder describe a full binary tree.

## 2. Problem it solves

Reconstruct a tree uniquely when preorder and postorder describe a full binary tree.

## 3. Core intuition

The second preorder key is the left subtree's root. Its location in postorder identifies where that subtree ends.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. The second preorder key is the left subtree's root. Its location in postorder identifies where that subtree ends.
3. Produce the result from the completed traversal.

## 6. Visual example

```text
    1
   / \
  2   3
 / \
4   5
```

## 7. Dry run

In preorder [1, 2, 4, 5, 3], the key 2 appears at index 2 in postorder [4, 5, 2, 3, 1]. The left subtree contains three nodes.

## 8. Python implementation

Start with `full_from_preorder_postorder` in [implementation.py](implementation.py). Produce the result from the completed traversal.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes and height H, expected time is O(N) and auxiliary space O(N + H).

## 10. Why the algorithm works

Fullness forces a nonleaf to have a left and right subtree. The left root boundary fixes their sizes and each recursive segment inherits fullness.

## 11. When to use it

Reconstruct a tree uniquely when preorder and postorder describe a full binary tree.

## 12. When not to use it

Recursive implementations can reach Python's recursion limit on skewed trees.

## 13. Common mistakes

Reject any split with only one child, where ordinary pre/post reconstruction is ambiguous.

## 14. Alternative approaches

An explicit stack avoids using Python call frames.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

The second preorder key is the left subtree's root. Its location in postorder identifies where that subtree ends. Reject any split with only one child, where ordinary pre/post reconstruction is ambiguous.
