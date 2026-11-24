# LCA Using Binary Lifting

**P2**

## 1. What is the algorithm?

Find the deepest ancestor shared by two vertices in logarithmic time.

## 2. Problem it solves

Find the deepest ancestor shared by two vertices in logarithmic time.

## 3. Core intuition

Align their depths, then greedily raise both by the largest jump that leaves them distinct.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Root the undirected tree and preprocess the indicated index.
2. Align their depths, then greedily raise both by the largest jump that leaves them distinct.
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

Nodes 3 and 2 begin one depth apart. Align 3 to 1. Then 1 and 2 have equal parents, so answer 0.

## 8. Python implementation

Start with `lca_binary_lifting` in [implementation.py](implementation.py). Return the result for each requested vertex or pair.

## 9. Time and space complexity

For N nodes, query time O(log(N + 1)), working space O(1), and preprocessing time and storage O(N log(N + 1)).

## 10. Why the algorithm works

At equal depth the ancestor sequences first coincide at LCA and stay equal above it. Safe jumps approach the final distinct pair, whose parent is LCA.

## 11. When to use it

Find the deepest ancestor shared by two vertices in logarithmic time.

## 12. When not to use it

The index assumes a fixed tree structure. Rebuild it after edges change.

## 13. Common mistakes

If alignment makes both nodes equal, return that node immediately.

## 14. Alternative approaches

Euler LCA uses a range-minimum query and answers in O(1) after comparable preprocessing.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Align their depths, then greedily raise both by the largest jump that leaves them distinct. If alignment makes both nodes equal, return that node immediately.
