# BST Search

**P1**

## 1. What is the algorithm?

Look up one key by comparing only along its possible search path.

## 2. Problem it solves

Look up one key by comparing only along its possible search path.

## 3. Core intuition

Choose the left child for a smaller key and the right child for a greater key.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Initialize the search or traversal at the root.
2. Choose the left child for a smaller key and the right child for a greater key.
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

Searching for 3 compares against 4, then 2, then 3.

## 8. Python implementation

Start with `bst_search` in [implementation.py](implementation.py). Return the selected value or updated result.

## 9. Time and space complexity

For height H, time is O(H + 1) and auxiliary space O(1). Balance gives H=O(log N) for N nodes, while a chain has H=N−1.

## 10. Why the algorithm works

At each comparison the ordering invariant excludes one complete subtree.

## 11. When to use it

Look up one key by comparing only along its possible search path.

## 12. When not to use it

The algorithm assumes a strict BST with distinct integer keys.

## 13. Common mistakes

Return the actual node if callers need its identity.

## 14. Alternative approaches

AVL or red-black trees keep the search height logarithmic.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Choose the left child for a smaller key and the right child for a greater key. Return the actual node if callers need its identity.
