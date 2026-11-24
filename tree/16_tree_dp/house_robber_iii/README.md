# House Robber III

**P2**

## 1. What is the algorithm?

Maximize the weighted value of a set with no parent-child conflict.

## 2. Problem it solves

Maximize the weighted value of a set with no parent-child conflict.

## 3. Core intuition

Compute take and skip totals separately, then combine independent choices from each child.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Root the tree and establish subproblem order.
2. Compute take and skip totals separately, then combine independent choices from each child.
3. Read the complete result from the computed states.

## 6. Visual example

```text
0 ─ 1 ─ 2
    |
    3
```

## 7. Dry run

A root of value 4 with a left grandchild of 5 can take both, for 9. Skipping the root instead can take the grandchild and the right child of value 3, for 8.

## 8. Python implementation

Start with `house_robber_iii` in [implementation.py](implementation.py). Read the complete result from the computed states.

## 9. Time and space complexity

For N nodes and height H, O(N) time and O(H + 1) stack space.

## 10. Why the algorithm works

When the node is selected, skipped child roots guarantee feasibility. When it is skipped, the larger child state is safe because branches are disjoint.

## 11. When to use it

Maximize the weighted value of a set with no parent-child conflict.

## 12. When not to use it

A deep skewed tree can exceed Python's recursion limit.

## 13. Common mistakes

Keep the skip result available even for a leaf with a negative value.

## 14. Alternative approaches

An explicit DFS stack can produce the same parent-before-child order.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Compute take and skip totals separately, then combine independent choices from each child. Keep the skip result available even for a leaf with a negative value.
