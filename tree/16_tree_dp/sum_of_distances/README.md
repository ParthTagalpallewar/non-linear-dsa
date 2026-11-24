# Sum of Distances in a Tree

**P2**

## 1. What is the algorithm?

Compute the distance total for every possible starting vertex.

## 2. Problem it solves

Compute the distance total for every possible starting vertex.

## 3. Core intuition

When shifting the root over an edge to a child containing K of N vertices, K distances shrink and N−K grow.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Root the tree and establish subproblem order.
2. When shifting the root over an edge to a child containing K of N vertices, K distances shrink and N−K grow.
3. Read the complete result from the computed states.

## 6. Visual example

```text
0 ─ 1 ─ 2
    |
    3
```

## 7. Dry run

From root 0 the total is 5. Shifting to 1 brings three vertices closer and one farther, yielding 5 + 4 − 6 = 3.

## 8. Python implementation

Start with `sum_of_distances` in [implementation.py](implementation.py). Read the complete result from the computed states.

## 9. Time and space complexity

For N nodes, O(N) time and O(N) auxiliary space. The rooted tree has N−1 undirected edges.

## 10. Why the algorithm works

For each edge, all paths to the child-side vertices become one edge shorter and all others become one edge longer. Applying this difference in preorder computes every root's exact answer.

## 11. When to use it

Compute the distance total for every possible starting vertex.

## 12. When not to use it

A graph with cycles needs a different state model.

## 13. Common mistakes

Subtree sizes must refer to the original rooting used for parent links.

## 14. Alternative approaches

Running BFS separately from every vertex is simple but takes O(N²) time.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

When shifting the root over an edge to a child containing K of N vertices, K distances shrink and N−K grow. Subtree sizes must refer to the original rooting used for parent links.
