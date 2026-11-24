# BST Deletion

**P1**

## 1. What is the algorithm?

Remove a key while preserving strict search order.

## 2. Problem it solves

Remove a key while preserving strict search order.

## 3. Core intuition

Splice out nodes with at most one child. For two children, copy the smallest right key and remove its old occurrence.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Initialize the search or traversal at the root.
2. Splice out nodes with at most one child. For two children, copy the smallest right key and remove its old occurrence.
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

Deleting 4 replaces its key with successor 6. The old node 6 gives way to its child 8.

## 8. Python implementation

Start with `bst_delete` in [implementation.py](implementation.py). Return the selected value or updated result.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For height H, time and recursive auxiliary space are O(H + 1).

## 10. Why the algorithm works

The successor is greater than every left key and smaller than every remaining right key. Splicing one child preserves the original ancestor bounds.

## 11. When to use it

Remove a key while preserving strict search order.

## 12. When not to use it

The algorithm assumes a strict BST with distinct integer keys.

## 13. Common mistakes

Reassign the child and root references returned by deletion.

## 14. Alternative approaches

AVL or red-black trees keep the search height logarithmic.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Splice out nodes with at most one child. For two children, copy the smallest right key and remove its old occurrence. Reassign the child and root references returned by deletion.
