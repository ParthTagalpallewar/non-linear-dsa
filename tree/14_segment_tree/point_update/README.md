# Segment Tree Point Update

**P2**

## 1. What is the algorithm?

Change one value and maintain every affected cached aggregate.

## 2. Problem it solves

Change one value and maintain every affected cached aggregate.

## 3. Core intuition

Read its actual value after lazy propagation and apply the difference to its singleton interval.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Represent the array with zero-based indices and half-open ranges.
2. Read its actual value after lazy propagation and apply the difference to its singleton interval.
3. Return the aggregate or keep the updated state for later queries.

## 6. Visual example

```text
[0,4)
├─ [0,2) ─ [0,1), [1,2)
└─ [2,4) ─ [2,3), [3,4)
```

## 7. Dry run

After adding 3 globally, [4, 3, 2] becomes [7, 6, 5]. Assigning −1 at index 1 applies delta −7.

## 8. Python implementation

Start with `point_update` in [implementation.py](implementation.py). Return the aggregate or keep the updated state for later queries.

## 9. Time and space complexity

For N values, query and update time is O(log(N + 1)). The tree stores O(N) values.

## 10. Why the algorithm works

Only intervals containing the updated leaf can change. Recombining precisely those ancestors restores all cached values.

## 11. When to use it

Change one value and maintain every affected cached aggregate.

## 12. When not to use it

Choose a simpler array for tiny input or rare queries.

## 13. Common mistakes

Use the difference between the requested value and the current value when reusing an additive update.

## 14. Alternative approaches

Use a Fenwick tree for additive prefix queries with smaller constants.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Read its actual value after lazy propagation and apply the difference to its singleton interval. Use the difference between the requested value and the current value when reusing an additive update.
