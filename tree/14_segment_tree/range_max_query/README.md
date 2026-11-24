# Range Max Query

**P2**

## 1. What is the algorithm?

Evaluate the max of a contiguous interval without scanning its elements.

## 2. Problem it solves

Evaluate the max of a contiguous interval without scanning its elements.

## 3. Core intuition

Combine cached values of maximal covered nodes and descend only on partially covered intervals.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Represent the array with zero-based indices and half-open ranges.
2. Combine cached values of maximal covered nodes and descend only on partially covered intervals.
3. Return the aggregate or keep the updated state for later queries.

## 6. Visual example

```text
[0,4)
├─ [0,2) ─ [0,1), [1,2)
└─ [2,4) ─ [2,3), [3,4)
```

## 7. Dry run

The range [1, 3) uses the two singleton values −2 and 7, giving 7.

## 8. Python implementation

Start with `range_max_query` in [implementation.py](implementation.py). Return the aggregate or keep the updated state for later queries.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N values, query and update time is O(log(N + 1)). The tree stores O(N) values. Segment-tree recursion adds O(log(N + 1)) auxiliary stack space.

## 10. Why the algorithm works

The selected tree intervals partition the query range and their associative summaries can be combined in any grouping.

## 11. When to use it

Evaluate the max of a contiguous interval without scanning its elements.

## 12. When not to use it

Choose a simpler array for tiny input or rare queries.

## 13. Common mistakes

Choose a matching aggregate at construction and handle an empty range according to its aggregate.

## 14. Alternative approaches

Use a Fenwick tree for additive prefix queries with smaller constants.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Combine cached values of maximal covered nodes and descend only on partially covered intervals. Choose a matching aggregate at construction and handle an empty range according to its aggregate.
