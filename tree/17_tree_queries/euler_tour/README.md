# Euler Tour

**P2**

## 1. What is the algorithm?

Linearize the full traversal of a rooted tree, including returns to parents.

## 2. Problem it solves

Linearize the full traversal of a rooted tree, including returns to parents.

## 3. Core intuition

Emit a node on its first visit and whenever DFS finishes one of its child subtrees.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Root the undirected tree and preprocess the indicated index.
2. Emit a node on its first visit and whenever DFS finishes one of its child subtrees.
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

The branches below 1 emit [1, 3, 1, 4, 1]. Returning to 0 then exploring 2 completes the walk.

## 8. Python implementation

Start with `euler_tour` in [implementation.py](implementation.py). Return the result for each requested vertex or pair.

## 9. Time and space complexity

For N vertices, time and auxiliary space O(N), and a nonempty tree emits 2N−1 positions.

## 10. Why the algorithm works

Every edge is crossed downward and upward exactly once. Each emitted vertex is the current endpoint of that crossing.

## 11. When to use it

Linearize the full traversal of a rooted tree, including returns to parents.

## 12. When not to use it

The index assumes a fixed tree structure. Rebuild it after edges change.

## 13. Common mistakes

Do not confuse the full Euler walk with the preorder-only array used for subtree intervals.

## 14. Alternative approaches

For very few queries, traverse the tree directly.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Emit a node on its first visit and whenever DFS finishes one of its child subtrees. Do not confuse the full Euler walk with the preorder-only array used for subtree intervals.
