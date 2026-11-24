# Root-to-Leaf Path Sum

**P1**

## 1. What is the algorithm?

Check whether a full root-to-leaf route reaches an exact sum.

## 2. Problem it solves

Check whether a full root-to-leaf route reaches an exact sum.

## 3. Core intuition

Subtract the current value from the remaining target and accept zero only at a leaf.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. Subtract the current value from the remaining target and accept zero only at a leaf.
3. Produce the result from the completed traversal.

## 6. Visual example

```text
    1
   / \
  2   3
 /
4
```

## 7. Dry run

Starting from target 7, visiting 1, then 2, then 4 leaves residuals 6, 4, and 0.

## 8. Python implementation

Start with `root_to_leaf_path_sum` in [implementation.py](implementation.py). Produce the result from the completed traversal.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes and height H, worst-case time is O(N) and auxiliary space O(H + 1), excluding output.

## 10. Why the algorithm works

The remaining target equals the original target minus the sum already consumed. A successful leaf therefore witnesses a complete route.

## 11. When to use it

Check whether a full root-to-leaf route reaches an exact sum.

## 12. When not to use it

Recursive implementations can reach Python's recursion limit on skewed trees.

## 13. Common mistakes

Values may be negative, so a negative residual alone does not justify pruning.

## 14. Alternative approaches

An explicit stack avoids using Python call frames.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Subtract the current value from the remaining target and accept zero only at a leaf. Values may be negative, so a negative residual alone does not justify pruning.
