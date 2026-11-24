# Heapify

**P1**

## 1. What is the algorithm?

Repair a single heap subtree after changing its root.

## 2. Problem it solves

Repair a single heap subtree after changing its root.

## 3. Core intuition

Compare both children and swap with the higher-priority one until the parent order holds.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Use the complete-tree index representation.
2. Compare both children and swap with the higher-priority one until the parent order holds.
3. Return the heap or selected item.

## 6. Visual example

```text
    1  (index 0)
   / \
  4   3  (indices 1, 2)
```

## 7. Dry run

Heapifying [8, 4, 2] in min order swaps 8 with 2 and stops at a leaf.

## 8. Python implementation

Start with `heapify` in [implementation.py](implementation.py). Return the heap or selected item.

## 9. Time and space complexity

For a heap with N items, worst-case O(log(N + 1)) time and O(1) space. A root already in order takes O(1).

## 10. Why the algorithm works

Promoting the better child fixes the old position, leaving only the displaced parent to repair in the selected child subtree.

## 11. When to use it

Repair a single heap subtree after changing its root.

## 12. When not to use it

A heap only guarantees order between parents and children. Use a sorted collection for arbitrary rank queries.

## 13. Common mistakes

Heapify one subtree only after its children already satisfy heap order.

## 14. Alternative approaches

Python's heapq is the standard-library choice for typical min-priority queues.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Compare both children and swap with the higher-priority one until the parent order holds. Heapify one subtree only after its children already satisfy heap order.
