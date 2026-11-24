# Fenwick Range Update

**P2**

## 1. What is the algorithm?

Add a constant to a range and still answer range sums efficiently.

## 2. Problem it solves

Add a constant to a range and still answer range sums efficiently.

## 3. Core intuition

A difference-array update changes only the interval endpoints. Track differences and index-weighted differences in two Fenwick trees.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Represent the array with zero-based indices and half-open ranges.
2. A difference-array update changes only the interval endpoints. Track differences and index-weighted differences in two Fenwick trees.
3. Return the aggregate or keep the updated state for later queries.

## 6. Visual example

```text
[0,4)
├─ [0,2) ─ [0,1), [1,2)
└─ [2,4) ─ [2,3), [3,4)
```

## 7. Dry run

Adding 3 to [1, 3) adds 3 to difference[1] and subtracts 3 from difference[3]. At end=3, its contribution is 3×3 − 1×3 = 6.

## 8. Python implementation

Start with `fenwick_range_update` in [implementation.py](implementation.py). Return the aggregate or keep the updated state for later queries.

## 9. Time and space complexity

For N values, query and update time is O(log(N + 1)). The tree stores O(N) values. Two arrays are needed, and operations use O(1) auxiliary space.

## 10. Why the algorithm works

A difference at index i contributes to each reconstructed value through end−1, appearing end−i times in prefix(end). Two Fenwick prefix queries evaluate that weighted sum.

## 11. When to use it

Add a constant to a range and still answer range sums efficiently.

## 12. When not to use it

Choose a simpler array for tiny input or rare queries.

## 13. Common mistakes

Skip the cancelling update when the right endpoint is the array length.

## 14. Alternative approaches

Lazy segment trees support richer range queries and update rules.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

A difference-array update changes only the interval endpoints. Track differences and index-weighted differences in two Fenwick trees. Skip the cancelling update when the right endpoint is the array length.
