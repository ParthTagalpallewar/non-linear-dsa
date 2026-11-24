# Subtree Dynamic Programming

**P2**

## 1. What is the algorithm?

Summarize each rooted subtree in one bottom-up pass.

## 2. Problem it solves

Summarize each rooted subtree in one bottom-up pass.

## 3. Core intuition

Seed a node with its own value and pass its subtotal to its parent after its children are complete.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Root the tree and establish subproblem order.
2. Seed a node with its own value and pass its subtotal to its parent after its children are complete.
3. Read the complete result from the computed states.

## 6. Visual example

```text
0 ─ 1 ─ 2
    |
    3
```

## 7. Dry run

With values [1, 2, −2, 4], node 1 receives −2 and 4 and forwards 4 to node 0, whose total is 5.

## 8. Python implementation

Start with `subtree_dp` in [implementation.py](implementation.py). Read the complete result from the computed states.

## 9. Time and space complexity

For N nodes, O(N) time and O(N) auxiliary space. The rooted tree has N−1 undirected edges.

## 10. Why the algorithm works

Every subtree equals its root plus disjoint child subtrees, so adding finalized child totals counts each element exactly once.

## 11. When to use it

Summarize each rooted subtree in one bottom-up pass.

## 12. When not to use it

A graph with cycles needs a different state model.

## 13. Common mistakes

Visit nodes in reverse preorder or a genuine postorder before propagating child values.

## 14. Alternative approaches

An explicit DFS stack can produce the same parent-before-child order.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Seed a node with its own value and pass its subtotal to its parent after its children are complete. Visit nodes in reverse preorder or a genuine postorder before propagating child values.
