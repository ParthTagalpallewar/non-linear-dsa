# Fenwick Range Sum Query

**P2**

## 1. What is the algorithm?

Perform a range sum without scanning the full input.

## 2. Problem it solves

Perform a range sum without scanning the full input.

## 3. Core intuition

Subtract the prefix ending at left from the prefix ending at right.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Represent the array with zero-based indices and half-open ranges.
2. Subtract the prefix ending at left from the prefix ending at right.
3. Return the aggregate or keep the updated state for later queries.

## 6. Visual example

```text
[0,4)
├─ [0,2) ─ [0,1), [1,2)
└─ [2,4) ─ [2,3), [3,4)
```

## 7. Dry run

In [4, −2, 5, 1], prefix(3)=7 and prefix(1)=4, so [1, 3) sums to 3.

## 8. Python implementation

Start with `fenwick_range_sum` in [implementation.py](implementation.py). Return the aggregate or keep the updated state for later queries.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N values, query and update time is O(log(N + 1)). The tree stores O(N) values. The index walk uses O(1) auxiliary space.

## 10. Why the algorithm works

The smaller prefix is fully contained in the larger, leaving precisely the requested range.

## 11. When to use it

Perform a range sum without scanning the full input.

## 12. When not to use it

Choose a simpler array for tiny input or rare queries.

## 13. Common mistakes

Public positions are zero-based and query endpoints are exclusive.

## 14. Alternative approaches

A segment tree supports additional associative aggregates such as minimum and maximum.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Subtract the prefix ending at left from the prefix ending at right. Public positions are zero-based and query endpoints are exclusive.
