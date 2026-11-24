# Fenwick Point Update

**P2**

## 1. What is the algorithm?

Perform a point update without scanning the full input.

## 2. Problem it solves

Perform a point update without scanning the full input.

## 3. Core intuition

Add the delta to each containing block by repeatedly adding the current index's low bit.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Represent the array with zero-based indices and half-open ranges.
2. Add the delta to each containing block by repeatedly adding the current index's low bit.
3. Return the aggregate or keep the updated state for later queries.

## 6. Visual example

```text
[0,4)
├─ [0,2) ─ [0,1), [1,2)
└─ [2,4) ─ [2,3), [3,4)
```

## 7. Dry run

Updating index 2 starts at internal index 3 and next visits index 4.

## 8. Python implementation

Start with `fenwick_point_update` in [implementation.py](implementation.py). Return the aggregate or keep the updated state for later queries.

## 9. Time and space complexity

For N values, query and update time is O(log(N + 1)). The tree stores O(N) values. The index walk uses O(1) auxiliary space.

## 10. Why the algorithm works

The internal jump advances to the first containing ancestor block, and every prefix uses each affected value at most once.

## 11. When to use it

Perform a point update without scanning the full input.

## 12. When not to use it

Choose a simpler array for tiny input or rare queries.

## 13. Common mistakes

Public positions are zero-based and query endpoints are exclusive.

## 14. Alternative approaches

A segment tree supports additional associative aggregates such as minimum and maximum.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Add the delta to each containing block by repeatedly adding the current index's low bit. Public positions are zero-based and query endpoints are exclusive.
