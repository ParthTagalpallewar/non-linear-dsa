# Heap Insertion

**P1**

## 1. What is the algorithm?

Insert an element without rebuilding the heap.

## 2. Problem it solves

Insert an element without rebuilding the heap.

## 3. Core intuition

Preserve the complete shape by appending at the end, then sift up.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Use the complete-tree index representation.
2. Preserve the complete shape by appending at the end, then sift up.
3. Return the heap or selected item.

## 6. Visual example

```text
    1  (index 0)
   / \
  4   3  (indices 1, 2)
```

## 7. Dry run

Appending 0 to [1, 4, 3] swaps it upward past 4 and then past 1.

## 8. Python implementation

Start with `heap_insert` in [implementation.py](implementation.py). Return the heap or selected item.

## 9. Time and space complexity

For N keys, worst-case time O(log(N + 1)), best-case O(1), and O(1) auxiliary space.

## 10. Why the algorithm works

Only the path from the appended position to the root can violate heap order.

## 11. When to use it

Insert an element without rebuilding the heap.

## 12. When not to use it

A heap only guarantees order between parents and children. Use a sorted collection for arbitrary rank queries.

## 13. Common mistakes

Sift toward the root after insertion.

## 14. Alternative approaches

Python's heapq is the standard-library choice for typical min-priority queues.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Preserve the complete shape by appending at the end, then sift up. Sift toward the root after insertion.
