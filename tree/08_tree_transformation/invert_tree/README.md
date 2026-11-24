# Invert Binary Tree

**P1**

## 1. What is the algorithm?

Reflect a binary tree horizontally.

## 2. Problem it solves

Reflect a binary tree horizontally.

## 3. Core intuition

Swap child references at every existing node.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. Swap child references at every existing node.
3. Produce the result from the completed traversal.

## 6. Visual example

```text
    1
   / \
  2   3
 /
4
```

## 7. Dry run

Root 1 still has value 1. Child 2 moves right, child 3 moves left, and node 4 becomes the right child of 2.

## 8. Python implementation

Start with `invert_tree` in [implementation.py](implementation.py). Produce the result from the completed traversal.

Run the example from the repository root with `uv run python -m tree.08_tree_transformation.invert_tree.implementation`.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes and height H, worst-case time is O(N) and auxiliary space O(H + 1), excluding output.

## 10. Why the algorithm works

A reflected path exchanges left with right at every step. The transformation visits each node once and applies exactly that exchange.

## 11. When to use it

Reflect a binary tree horizontally.

## 12. When not to use it

Choose a mirror copy when other code must retain the original structure.

## 13. Common mistakes

Pointers are modified in place, so callers sharing the root see the new structure.

## 14. Alternative approaches

A mirror copy preserves both versions simultaneously.

## 15. Practice problems

- LeetCode #226, Easy. Swap children at every node. [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Swap child references at every existing node. Pointers are modified in place, so callers sharing the root see the new structure.
