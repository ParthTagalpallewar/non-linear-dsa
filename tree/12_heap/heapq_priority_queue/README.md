# Priority Queue Using heapq

**P1**

## 1. What is the algorithm?

Retrieve the next available task by priority with stable ties.

## 2. Problem it solves

Retrieve the next available task by priority with stable ties.

## 3. Core intuition

Store (priority, arrival index, payload) tuples in a standard-library min-heap.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Use the complete-tree index representation.
2. Store (priority, arrival index, payload) tuples in a standard-library min-heap.
3. Return the heap or selected item.

## 6. Visual example

```text
    1  (index 0)
   / \
  4   3  (indices 1, 2)
```

## 7. Dry run

Push (1, 0, first) and (1, 1, second). The index places first ahead of second.

## 8. Python implementation

Start with `heapq_priority_queue` in [implementation.py](implementation.py). Return the heap or selected item.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N tasks, heap build is O(N), each pop is O(log(N + 1)), total O(N log(N + 1)) time and O(N) auxiliary space.

## 10. Why the algorithm works

Tuple comparison first considers priority, and distinct arrival indices resolve ties without depending on payload ordering.

## 11. When to use it

Retrieve the next available task by priority with stable ties.

## 12. When not to use it

A heap only guarantees order between parents and children. Use a sorted collection for arbitrary rank queries.

## 13. Common mistakes

Supply a tie-breaker to keep equal-priority records stable and avoid comparing arbitrary payloads.

## 14. Alternative approaches

Use sorted when all records are known and no interleaved pushes or pops are needed.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Store (priority, arrival index, payload) tuples in a standard-library min-heap. Supply a tie-breaker to keep equal-priority records stable and avoid comparing arbitrary payloads.
