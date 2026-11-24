# Segment Tree Construction

**P2**

## 1. What is the algorithm?

Precompute a reusable index for associative interval queries.

## 2. Problem it solves

Precompute a reusable index for associative interval queries.

## 3. Core intuition

Split the interval in half until each leaf stores one element, then combine child results on return.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Represent the array with zero-based indices and half-open ranges.
2. Split the interval in half until each leaf stores one element, then combine child results on return.
3. Return the aggregate or keep the updated state for later queries.

## 6. Visual example

```text
[0,4)
├─ [0,2) ─ [0,1), [1,2)
└─ [2,4) ─ [2,3), [3,4)
```

## 7. Dry run

For [4, −2, 7, 3], the two child sums are 2 and 10, and the root stores 12.

## 8. Python implementation

Start with `segment_tree_construction` in [implementation.py](implementation.py). Return the aggregate or keep the updated state for later queries.

## 9. Time and space complexity

For N items, O(N) build time and storage, with O(log(N + 1)) stack space.

## 10. Why the algorithm works

Each internal interval is partitioned into disjoint children, so combining their summaries exactly represents the whole segment.

## 11. When to use it

Precompute a reusable index for associative interval queries.

## 12. When not to use it

Choose a simpler array for tiny input or rare queries.

## 13. Common mistakes

Tree indices address summaries, whereas interval bounds address original array positions.

## 14. Alternative approaches

Use a Fenwick tree for additive prefix queries with smaller constants.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Split the interval in half until each leaf stores one element, then combine child results on return. Tree indices address summaries, whereas interval bounds address original array positions.
