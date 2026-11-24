# Fenwick Prefix Sum Query

**P2**

## 1. What is the algorithm?

Perform a prefix sum without scanning the full input.

## 2. Problem it solves

Perform a prefix sum without scanning the full input.

## 3. Core intuition

Take the block ending at end and clear its lowest set bit, repeating until zero.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Represent the array with zero-based indices and half-open ranges.
2. Take the block ending at end and clear its lowest set bit, repeating until zero.
3. Return the aggregate or keep the updated state for later queries.

## 6. Visual example

```text
[0,4)
├─ [0,2) ─ [0,1), [1,2)
└─ [2,4) ─ [2,3), [3,4)
```

## 7. Dry run

For [4, −2, 5, 1], prefix end 3 uses blocks ending at 3 and 2 for a sum of 7.

## 8. Python implementation

Start with `fenwick_prefix_sum` in [implementation.py](implementation.py). Return the aggregate or keep the updated state for later queries.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N values, query and update time is O(log(N + 1)). The tree stores O(N) values. The index walk uses O(1) auxiliary space.

## 10. Why the algorithm works

The blocks visited by clearing the low bit form a disjoint partition of the requested prefix.

## 11. When to use it

Perform a prefix sum without scanning the full input.

## 12. When not to use it

Choose a simpler array for tiny input or rare queries.

## 13. Common mistakes

Public positions are zero-based and query endpoints are exclusive.

## 14. Alternative approaches

A segment tree supports additional associative aggregates such as minimum and maximum.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Take the block ending at end and clear its lowest set bit, repeating until zero. Public positions are zero-based and query endpoints are exclusive.
