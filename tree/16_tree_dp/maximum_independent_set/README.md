# Maximum Independent Set on a Tree

**P2**

## 1. What is the algorithm?

Pick the largest collection of vertices containing no edge between selected vertices.

## 2. Problem it solves

Pick the largest collection of vertices containing no edge between selected vertices.

## 3. Core intuition

Keep two optima per node: selecting it forbids selecting its children, while skipping it allows either child state.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Root the tree and establish subproblem order.
2. Keep two optima per node: selecting it forbids selecting its children, while skipping it allows either child state.
3. Read the complete result from the computed states.

## 6. Visual example

```text
0 ─ 1 ─ 2
    |
    3
```

## 7. Dry run

For the star centered at 1, choosing 1 gives size one. Skipping it allows leaves 0, 2, and 3, giving size three.

## 8. Python implementation

Start with `maximum_independent_set` in [implementation.py](implementation.py). Read the complete result from the computed states.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes, O(N) time and O(N) auxiliary space. The rooted tree has N−1 undirected edges.

## 10. Why the algorithm works

After fixing the parent's decision, distinct child subtrees have no cross-edges. Each can independently contribute its compatible optimum.

## 11. When to use it

Pick the largest collection of vertices containing no edge between selected vertices.

## 12. When not to use it

A graph with cycles needs a different state model.

## 13. Common mistakes

A parent's skip state must choose the better option independently for each child.

## 14. Alternative approaches

An explicit DFS stack can produce the same parent-before-child order.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Keep two optima per node: selecting it forbids selecting its children, while skipping it allows either child state. A parent's skip state must choose the better option independently for each child.
