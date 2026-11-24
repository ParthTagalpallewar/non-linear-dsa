# Heap Sort

**P1**

## 1. What is the algorithm?

Sort an array in place with an O(N log N) worst-case bound.

## 2. Problem it solves

Sort an array in place with an O(N log N) worst-case bound.

## 3. Core intuition

Move the maximum root to the end of the remaining heap, gradually building the sorted suffix.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Use the complete-tree index representation.
2. Move the maximum root to the end of the remaining heap, gradually building the sorted suffix.
3. Return the heap or selected item.

## 6. Visual example

```text
    1  (index 0)
   / \
  4   3  (indices 1, 2)
```

## 7. Dry run

Heap [4, 1, 3] trades 4 with index 2, freezes that position, and repairs the length-two heap.

## 8. Python implementation

Start with `heap_sort` in [implementation.py](implementation.py). Return the heap or selected item.

Run the example from the repository root with `uv run python -m tree.12_heap.heap_sort.implementation`.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N items, worst-case O(N log(N + 1)) time and O(1) auxiliary space. Building the first heap is O(N).

## 10. Why the algorithm works

The frozen suffix contains the largest keys already sorted. The unfrozen prefix remains a max heap after each repair.

## 11. When to use it

Sort an array in place with an O(N log N) worst-case bound.

## 12. When not to use it

A heap only guarantees order between parents and children. Use a sorted collection for arbitrary rank queries.

## 13. Common mistakes

Never include a frozen position in a later sift.

## 14. Alternative approaches

Python's built-in sort is stable and exploits runs, with additional working memory.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Move the maximum root to the end of the remaining heap, gradually building the sorted suffix. Never include a frozen position in a later sift.
