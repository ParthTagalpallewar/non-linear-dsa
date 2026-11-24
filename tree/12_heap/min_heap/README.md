# Min Heap

**P1**

## 1. What is the algorithm?

Repeatedly access or remove the smallest key.

## 2. Problem it solves

Repeatedly access or remove the smallest key.

## 3. Core intuition

Maintain the heap order in every parent-child pair while keeping the complete shape.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Use the complete-tree index representation.
2. Maintain the heap order in every parent-child pair while keeping the complete shape.
3. Return the heap or selected item.

## 6. Visual example

```text
    1  (index 0)
   / \
  4   3  (indices 1, 2)
```

## 7. Dry run

For keys [4, 1, 3], the smallest key reaches the root. Removing it leaves a heap of two keys.

## 8. Python implementation

Start with `min_heap` in [implementation.py](implementation.py). Return the heap or selected item.

## 9. Time and space complexity

Build N keys in O(N) time and storage. Peek is O(1), push/pop take O(log(N + 1)) worst-case time and O(1) working space.

## 10. Why the algorithm works

Transitivity over the chain of parent links proves that no descendant outranks the root. Local sift operations repair the sole path where order may fail.

## 11. When to use it

Repeatedly access or remove the smallest key.

## 12. When not to use it

A heap only guarantees order between parents and children. Use a sorted collection for arbitrary rank queries.

## 13. Common mistakes

A heap array is not generally sorted.

## 14. Alternative approaches

Python's heapq is the standard-library choice for typical min-priority queues.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Maintain the heap order in every parent-child pair while keeping the complete shape. A heap array is not generally sorted.
