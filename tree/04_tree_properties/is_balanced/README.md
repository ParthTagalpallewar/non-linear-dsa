# Balanced Binary Tree Check

**P1**

## 1. What is the algorithm?

Detect whether the height difference stays within one throughout a tree.

## 2. Problem it solves

Detect whether the height difference stays within one throughout a tree.

## 3. Core intuition

Compute height once per subtree, returning a sentinel when any descendant violates the balance rule.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle a missing root.
2. Compute height once per subtree, returning a sentinel when any descendant violates the balance rule.
3. Return the finalized measurement or predicate.

## 6. Visual example

```text
    1
   / \
  2   3
 /
4
```

## 7. Dry run

In the example node 2's two child heights are 1 and 0. At the root the child heights are 2 and 1, so both pass.

## 8. Python implementation

Start with `is_balanced` in [implementation.py](implementation.py). Return the finalized measurement or predicate.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes and tree height H, time is O(N) and stack space O(H + 1).

## 10. Why the algorithm works

A nonnegative return guarantees a balanced subtree and gives its actual height. The sentinel preserves any violation as results move toward the root.

## 11. When to use it

Detect whether the height difference stays within one throughout a tree.

## 12. When not to use it

Inputs must be proper trees without shared children or cycles.

## 13. Common mistakes

Checking only the root can miss an imbalanced descendant.

## 14. Alternative approaches

An explicit stack can replace recursive traversal when depth is unbounded.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Compute height once per subtree, returning a sentinel when any descendant violates the balance rule. Checking only the root can miss an imbalanced descendant.
