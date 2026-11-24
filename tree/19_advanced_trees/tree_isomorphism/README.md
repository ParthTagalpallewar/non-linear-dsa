# Unrooted Tree Isomorphism

**P3**

## 1. What is the algorithm?

Decide whether two unlabeled trees have the same shape.

## 2. Problem it solves

Decide whether two unlabeled trees have the same shape.

## 3. Core intuition

Find the one or two central vertices by trimming leaves. Intern each rooted node's sorted child-shape IDs using a dictionary shared by both trees.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Remove leaf layers until at most two vertices remain.
2. Root the tree at each remaining center.
3. Encode shapes bottom-up and test whether any rooted shapes match.

## 6. Visual example

```text
    0
   / \
  1   2
 / \
3   4
```

## 7. Dry run

On the pictured tree, trimming leaves 2, 3, and 4 leaves centers 0 and 1. Trying both roots removes any dependence on original IDs.

## 8. Python implementation

Start with `tree_isomorphism` in [implementation.py](implementation.py). Encode shapes bottom-up and test whether any rooted shapes match.

## 9. Time and space complexity

For N vertices and maximum degree D, expected time O(N log(D + 1)) and auxiliary space O(N), because at most two roots per tree are encoded.

## 10. Why the algorithm works

An isomorphism preserves distances and therefore centers. At a fixed root, equality holds precisely when the multisets of child shapes agree recursively.

## 11. When to use it

Decide whether two unlabeled trees have the same shape.

## 12. When not to use it

Use these routines on undirected trees with symmetric adjacency and integer IDs 0 through N−1.

## 13. Common mistakes

Use one shared interning table. Independent identifier assignments could equate unrelated shapes.

## 14. Alternative approaches

A sorted parenthesized representation is simple but repeated string construction can cost quadratic time on a long chain.

## 15. Practice problems

**Original exercise · P3.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Find the one or two central vertices by trimming leaves. Intern each rooted node's sorted child-shape IDs using a dictionary shared by both trees. Use one shared interning table. Independent identifier assignments could equate unrelated shapes.
