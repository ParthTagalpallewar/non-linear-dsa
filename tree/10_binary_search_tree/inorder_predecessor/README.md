# Inorder Predecessor

**P1**

## 1. What is the algorithm?

Find the greatest key strictly below the target, even if the target is missing.

## 2. Problem it solves

Find the greatest key strictly below the target, even if the target is missing.

## 3. Core intuition

Keep the nearest strict lower candidate and search its right subtree for a better one.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Initialize the search or traversal at the root.
2. Keep the nearest strict lower candidate and search its right subtree for a better one.
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

With sorted keys [1, 2, 3, 4, 6, 8], target 5 gives 4. Requires strict inequality.

## 8. Python implementation

Start with `inorder_predecessor` in [implementation.py](implementation.py). Return the selected value or updated result.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For height H, time is O(H + 1) and auxiliary space O(1). Balance gives H=O(log N) for N nodes, while a chain has H=N−1.

## 10. Why the algorithm works

If the current key is below the target, a larger qualifying key must lie right. The discarded subtree cannot contain a better feasible key.

## 11. When to use it

Find the greatest key strictly below the target, even if the target is missing.

## 12. When not to use it

The algorithm assumes a strict BST with distinct integer keys.

## 13. Common mistakes

Distinguish strict predecessor and successor from inclusive floor and ceiling.

## 14. Alternative approaches

AVL or red-black trees keep the search height logarithmic.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Keep the nearest strict lower candidate and search its right subtree for a better one. Distinguish strict predecessor and successor from inclusive floor and ceiling.
