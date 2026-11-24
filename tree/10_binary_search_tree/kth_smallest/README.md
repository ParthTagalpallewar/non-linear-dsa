# Kth Smallest Element

**P1**

## 1. What is the algorithm?

Select a key by rank without flattening the whole tree.

## 2. Problem it solves

Select a key by rank without flattening the whole tree.

## 3. Core intuition

Traverse in ascending order and stop after k values.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Initialize the search or traversal at the root.
2. Traverse in ascending order and stop after k values.
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

The sequence starts 1, 2, 3, so rank two gives 2.

## 8. Python implementation

Start with `kth_smallest` in [implementation.py](implementation.py). Return the selected value or updated result.

## 9. Time and space complexity

For tree height H and valid rank K, time O(H + K), auxiliary space O(H + 1). An invalid oversized rank scans all N nodes.

## 10. Why the algorithm works

BST ordering makes each inorder visit the next smallest remaining key, and reversing inorder makes it the next largest.

## 11. When to use it

Select a key by rank without flattening the whole tree.

## 12. When not to use it

The algorithm assumes a strict BST with distinct integer keys.

## 13. Common mistakes

Treat k as one-indexed and check exhaustion.

## 14. Alternative approaches

Subtree sizes support O(H + 1) rank selection per query.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Traverse in ascending order and stop after k values. Treat k as one-indexed and check exhaustion.
