# BST Insertion

**P1**

## 1. What is the algorithm?

Add an ordered key while retaining the BST invariant.

## 2. Problem it solves

Add an ordered key while retaining the BST invariant.

## 3. Core intuition

Use the lookup path and attach a node at the first missing child.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Initialize the search or traversal at the root.
2. Use the lookup path and attach a node at the first missing child.
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

To insert 3 into 4→left 2, choose the right child of 2 and attach there.

## 8. Python implementation

Start with `bst_insert` in [implementation.py](implementation.py). Return the selected value or updated result.

## 9. Time and space complexity

For height H, time is O(H + 1) and auxiliary space O(1). Balance gives H=O(log N) for N nodes, while a chain has H=N−1.

## 10. Why the algorithm works

Every comparison adds a constraint on the insertion position. The chosen null slot satisfies all ancestor constraints.

## 11. When to use it

Add an ordered key while retaining the BST invariant.

## 12. When not to use it

The algorithm assumes a strict BST with distinct integer keys.

## 13. Common mistakes

Return the new root when inserting into an empty tree and define a duplicate policy.

## 14. Alternative approaches

AVL or red-black trees keep the search height logarithmic.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Use the lookup path and attach a node at the first missing child. Return the new root when inserting into an empty tree and define a duplicate policy.
