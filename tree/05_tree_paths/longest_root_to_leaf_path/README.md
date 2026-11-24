# Longest Root-to-Leaf Path

**P1**

## 1. What is the algorithm?

Keep the deepest complete branch.

## 2. Problem it solves

Keep the deepest complete branch.

## 3. Core intuition

Record parents and track the first deepest leaf, then reconstruct its route once.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. Record parents and track the first deepest leaf, then reconstruct its route once.
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

The leaf routes are [1, 2, 4] and [1, 3]. The result is [1, 2, 4].

## 8. Python implementation

Start with `longest_root_to_leaf_path` in [implementation.py](implementation.py). Produce the result from the completed traversal.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes, time and auxiliary space are O(N) including the parent map.

## 10. Why the algorithm works

A root-to-leaf route is in one-to-one correspondence with its final leaf. Each leaf is visited exactly once.

## 11. When to use it

Keep the deepest complete branch.

## 12. When not to use it

Recursive implementations can reach Python's recursion limit on skewed trees.

## 13. Common mistakes

Count a node as a leaf only when both child references are absent.

## 14. Alternative approaches

An explicit stack avoids using Python call frames.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Record parents and track the first deepest leaf, then reconstruct its route once. Count a node as a leaf only when both child references are absent.
