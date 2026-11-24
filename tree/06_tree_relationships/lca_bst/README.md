# Lowest Common Ancestor in a BST

**P1**

## 1. What is the algorithm?

Locate the deepest common search point for two keys in a strict BST.

## 2. Problem it solves

Locate the deepest common search point for two keys in a strict BST.

## 3. Core intuition

Descend only when both keys lie on the same side. At the first split, verify that both keys exist.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. Descend only when both keys lie on the same side. At the first split, verify that both keys exist.
3. Produce the result from the completed traversal.

## 6. Visual example

```text
  2
 / \
1   3
```

## 7. Dry run

In a BST rooted at 2 with children 1 and 3, searching for the pair 1 and 3 splits immediately at 2.

## 8. Python implementation

Start with `lca_bst` in [implementation.py](implementation.py). Produce the result from the completed traversal.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For height H, time O(H + 1) and auxiliary space O(1). A balanced tree gives O(log(N + 1)) time for N nodes.

## 10. Why the algorithm works

The BST invariant excludes both keys from one child whenever they lie on the same side. A split or equality prevents any child from containing both.

## 11. When to use it

Locate the deepest common search point for two keys in a strict BST.

## 12. When not to use it

Use general LCA for unordered trees or duplicate keys.

## 13. Common mistakes

A split can occur even when a key is absent. Check presence if the caller cannot guarantee it.

## 14. Alternative approaches

An explicit stack avoids using Python call frames.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Descend only when both keys lie on the same side. At the first split, verify that both keys exist. A split can occur even when a key is absent. Check presence if the caller cannot guarantee it.
