# Binary Lifting

**P2**

## 1. What is the algorithm?

Preprocess a static tree to support upward jumps and LCA.

## 2. Problem it solves

Preprocess a static tree to support upward jumps and LCA.

## 3. Core intuition

The 2^j ancestor is the 2^(j−1) ancestor of the 2^(j−1) ancestor.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Root the undirected tree and preprocess the indicated index.
2. The 2^j ancestor is the 2^(j−1) ancestor of the 2^(j−1) ancestor.
3. Return the result for each requested vertex or pair.

## 6. Visual example

```text
    0
   / \
  1   2
 / \
3   4
```

## 7. Dry run

On a five-node chain rooted at one end, the other end's jumps of 1, 2, and 4 reach progressively higher nodes.

## 8. Python implementation

Start with `binary_lifting` in [implementation.py](implementation.py). Return the result for each requested vertex or pair.

## 9. Time and space complexity

For N nodes, preprocessing takes O(N log(N + 1)) time and storage. A jump query uses O(log(N + 1)) time and O(1) working space.

## 10. Why the algorithm works

A composition of two equal jumps skips exactly twice as many edges, so induction over columns gives each entry.

## 11. When to use it

Preprocess a static tree to support upward jumps and LCA.

## 12. When not to use it

The index assumes a fixed tree structure. Rebuild it after edges change.

## 13. Common mistakes

Store an explicit sentinel for ancestors above the root.

## 14. Alternative approaches

For very few queries, traverse the tree directly.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

The 2^j ancestor is the 2^(j−1) ancestor of the 2^(j−1) ancestor. Store an explicit sentinel for ancestors above the root.
