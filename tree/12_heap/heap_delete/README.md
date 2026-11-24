# Heap Deletion

**P1**

## 1. What is the algorithm?

Remove the extreme value while preserving the heap.

## 2. Problem it solves

Remove the extreme value while preserving the heap.

## 3. Core intuition

Move the last value to the root, shorten the array, and sift down.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Use the complete-tree index representation.
2. Move the last value to the root, shorten the array, and sift down.
3. Return the heap or selected item.

## 6. Visual example

```text
    1  (index 0)
   / \
  4   3  (indices 1, 2)
```

## 7. Dry run

Removing 1 from [1, 4, 3] moves 3 to the root and it already outranks 4.

## 8. Python implementation

Start with `heap_delete` in [implementation.py](implementation.py). Return the heap or selected item.

## 9. Time and space complexity

For N keys, worst-case time O(log(N + 1)), best-case O(1), and O(1) auxiliary space.

## 10. Why the algorithm works

Deleting the last array position preserves completeness. All remaining order violations are along the replacement's downward path.

## 11. When to use it

Remove the extreme value while preserving the heap.

## 12. When not to use it

A heap only guarantees order between parents and children. Use a sorted collection for arbitrary rank queries.

## 13. Common mistakes

Handle deletion from an empty heap, and skip sifting after removing its last item.

## 14. Alternative approaches

Python's heapq is the standard-library choice for typical min-priority queues.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Move the last value to the root, shorten the array, and sift down. Handle deletion from an empty heap, and skip sifting after removing its last item.
