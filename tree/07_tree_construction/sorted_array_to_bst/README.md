# Convert Sorted Array to Balanced BST

**P1**

## 1. What is the algorithm?

Create a shallow search tree directly from sorted keys.

## 2. Problem it solves

Create a shallow search tree directly from sorted keys.

## 3. Core intuition

Choose the median as the root so both child subproblems contain nearly equal numbers of elements.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. Choose the median as the root so both child subproblems contain nearly equal numbers of elements.
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

For [1, 2, 3, 4, 5], split at key 3. The left interval produces 2 with child 1, and the right produces 5 with child 4.

## 8. Python implementation

Start with `sorted_array_to_bst` in [implementation.py](implementation.py). Produce the result from the completed traversal.

## 9. Time and space complexity

For N keys, O(N) construction and validation time, O(log(N + 1)) auxiliary stack space, and O(N) output space.

## 10. Why the algorithm works

The index ranges preserve the strict ordering invariant. Two near-equal subproblem sizes have resulting heights differing by at most one.

## 11. When to use it

Create a shallow search tree directly from sorted keys.

## 12. When not to use it

The caller needs sorted distinct keys or must prepare them first.

## 13. Common mistakes

Pass index bounds rather than creating slices at every call.

## 14. Alternative approaches

AVL insertion can maintain balance as unsorted keys arrive one at a time.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Choose the median as the root so both child subproblems contain nearly equal numbers of elements. Pass index bounds rather than creating slices at every call.
