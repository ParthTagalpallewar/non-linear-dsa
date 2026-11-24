# Binary Indexed Tree Construction

**P2**

## 1. What is the algorithm?

Build a binary indexed tree without inserting each value individually.

## 2. Problem it solves

Build a binary indexed tree without inserting each value individually.

## 3. Core intuition

Starting with singleton values, add each completed block to the next larger block it belongs to.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Represent the array with zero-based indices and half-open ranges.
2. Starting with singleton values, add each completed block to the next larger block it belongs to.
3. Return the aggregate or keep the updated state for later queries.

## 6. Visual example

```text
[0,4)
├─ [0,2) ─ [0,1), [1,2)
└─ [2,4) ─ [2,3), [3,4)
```

## 7. Dry run

Index 1 contributes 3 to index 2. Index 2 now stores 4 and contributes it to index 4. Index 3 contributes another 4 to index 4.

## 8. Python implementation

Start with `fenwick_construction` in [implementation.py](implementation.py). Return the aggregate or keep the updated state for later queries.

Run the example from the repository root with `uv run python -m tree.15_fenwick_tree.fenwick_construction.implementation`.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N values, time and storage are O(N), with O(1) working space beyond the index.

## 10. Why the algorithm works

Every block's parent index is larger, so ascending iteration propagates each interval's completed sum exactly once.

## 11. When to use it

Build a binary indexed tree without inserting each value individually.

## 12. When not to use it

Choose a simpler array for tiny input or rare queries.

## 13. Common mistakes

Keep index zero as a sentinel and convert public zero-based positions at the boundary.

## 14. Alternative approaches

Repeated point additions build the index in O(N log N) time.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Starting with singleton values, add each completed block to the next larger block it belongs to. Keep index zero as a sentinel and convert public zero-based positions at the boundary.
