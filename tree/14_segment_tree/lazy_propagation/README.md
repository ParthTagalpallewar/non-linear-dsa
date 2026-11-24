# Lazy Propagation

**P2**

## 1. What is the algorithm?

Avoid touching every element when adding the same value to a range.

## 2. Problem it solves

Avoid touching every element when adding the same value to a range.

## 3. Core intuition

On a full cover, adjust the cached aggregate and store the pending delta. Push it to child segments only before descending.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Represent the array with zero-based indices and half-open ranges.
2. On a full cover, adjust the cached aggregate and store the pending delta. Push it to child segments only before descending.
3. Return the aggregate or keep the updated state for later queries.

## 6. Visual example

```text
[0,4)
├─ [0,2) ─ [0,1), [1,2)
└─ [2,4) ─ [2,3), [3,4)
```

## 7. Dry run

Adding 2 to all four items changes the sum from 10 to 18 at the root alone. A later update confined to [1, 3) pushes that tag before inspecting children.

## 8. Python implementation

Start with `lazy_propagation` in [implementation.py](implementation.py). Return the aggregate or keep the updated state for later queries.

Run the example from the repository root with `uv run python -m tree.14_segment_tree.lazy_propagation.implementation`.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N values, query and update time is O(log(N + 1)). The tree stores O(N) values. For U updates after build, total time O(N + U log(N + 1)) excluding output.

## 10. Why the algorithm works

Each node's summary already reflects its own tag. A push transfers that logical change to each child exactly once, preserving equivalence to individual updates.

## 11. When to use it

Avoid touching every element when adding the same value to a range.

## 12. When not to use it

Different update operations require a different tag composition rule. Range assignment cannot use additive tags unchanged.

## 13. Common mistakes

Multiply the delta by covered length for sums. Min and max move by just the delta.

## 14. Alternative approaches

Use a Fenwick tree for additive prefix queries with smaller constants.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

On a full cover, adjust the cached aggregate and store the pending delta. Push it to child segments only before descending. Multiply the delta by covered length for sums. Min and max move by just the delta.
