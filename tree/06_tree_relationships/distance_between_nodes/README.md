# Distance Between Two Nodes

**P1**

## 1. What is the algorithm?

Measure the number of edges between two identified nodes.

## 2. Problem it solves

Measure the number of edges between two identified nodes.

## 3. Core intuition

Store distances along one ancestor chain, then climb from the other endpoint until the chains intersect.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. Store distances along one ancestor chain, then climb from the other endpoint until the chains intersect.
3. Produce the result from the completed traversal.

## 6. Visual example

```text
    1
   / \
  2   3
 /
4
```

## 7. Dry run

The map from 4 is {4:0, 2:1, 1:2}. Node 3 takes one step to 1, so the distance is 3.

## 8. Python implementation

Start with `distance_between_nodes` in [implementation.py](implementation.py). Produce the result from the completed traversal.

## 9. Time and space complexity

For N nodes, worst-case time and auxiliary space are O(N) due to parent indexing.

## 10. Why the algorithm works

The unique path goes upward to the lowest common ancestor and then downward. The two counted segments share no edges.

## 11. When to use it

Measure the number of edges between two identified nodes.

## 12. When not to use it

Recursive implementations can reach Python's recursion limit on skewed trees.

## 13. Common mistakes

Distance counts edges rather than nodes.

## 14. Alternative approaches

For many queries, preprocess LCA and use depth[u] + depth[v] − 2 depth[lca].

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Store distances along one ancestor chain, then climb from the other endpoint until the chains intersect. Distance counts edges rather than nodes.
