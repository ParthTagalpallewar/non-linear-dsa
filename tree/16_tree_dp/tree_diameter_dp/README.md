# Tree Diameter Using DP

**P2**

## 1. What is the algorithm?

Measure the longest simple route through an undirected tree.

## 2. Problem it solves

Measure the longest simple route through an undirected tree.

## 3. Core intuition

Compute the two longest downward arms from distinct children for every vertex.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Root the tree and establish subproblem order.
2. Compute the two longest downward arms from distinct children for every vertex.
3. Read the complete result from the computed states.

## 6. Visual example

```text
0 ─ 1 ─ 2
    |
    3
```

## 7. Dry run

At node 1, the arms to 2 and 3 have length one, giving a two-edge route between those leaves.

## 8. Python implementation

Start with `tree_diameter_dp` in [implementation.py](implementation.py). Read the complete result from the computed states.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes, O(N) time and O(N) auxiliary space. The rooted tree has N−1 undirected edges.

## 10. Why the algorithm works

Every simple route has a unique highest vertex relative to the chosen root. Its length is the sum of two downward arms, allowing one empty arm.

## 11. When to use it

Measure the longest simple route through an undirected tree.

## 12. When not to use it

A graph with cycles needs a different state model.

## 13. Common mistakes

Maintain two lengths from separately processed children, even if the lengths are equal.

## 14. Alternative approaches

Two BFS sweeps also compute diameter on an unweighted tree.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Compute the two longest downward arms from distinct children for every vertex. Maintain two lengths from separately processed children, even if the lengths are equal.
