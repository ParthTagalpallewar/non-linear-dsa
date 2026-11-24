# Build Heap

**P1**

## 1. What is the algorithm?

Construct a heap of all supplied values.

## 2. Problem it solves

Construct a heap of all supplied values.

## 3. Core intuition

Repair parents from the bottom upward so each sift starts with two valid child heaps.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Use the complete-tree index representation.
2. Repair parents from the bottom upward so each sift starts with two valid child heaps.
3. Return the heap or selected item.

## 6. Visual example

```text
    1  (index 0)
   / \
  4   3  (indices 1, 2)
```

## 7. Dry run

For [5, 2, 2, 1, 8], sift index 1 to position 3, then sift 5 from the root toward a leaf.

## 8. Python implementation

Start with `build_heap` in [implementation.py](implementation.py). Return the heap or selected item.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N keys, time O(N) and output space O(N), with O(1) working space. At most about N/2^(h+1) nodes have height h.

## 10. Why the algorithm works

Leaves are heaps initially. After fixing a parent, its whole subtree is a heap, extending the induction up to the root.

## 11. When to use it

Construct a heap of all supplied values.

## 12. When not to use it

A heap only guarantees order between parents and children. Use a sorted collection for arbitrary rank queries.

## 13. Common mistakes

Bottom-up construction starts at the last internal node, not the last leaf.

## 14. Alternative approaches

Inserting all N items individually can cost O(N log N).

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Repair parents from the bottom upward so each sift starts with two valid child heaps. Bottom-up construction starts at the last internal node, not the last leaf.
