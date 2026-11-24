# Nodes at Distance K

**P1**

## 1. What is the algorithm?

Find every node exactly k undirected edges from a target.

## 2. Problem it solves

Find every node exactly k undirected edges from a target.

## 3. Core intuition

Treat parent and children as neighbors, then stop BFS branches at the desired distance.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. Treat parent and children as neighbors, then stop BFS branches at the desired distance.
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

Starting at node 2, layer zero contains 2, layer one contains 4 and 1, and layer two contains 3.

## 8. Python implementation

Start with `nodes_at_distance_k` in [implementation.py](implementation.py). Produce the result from the completed traversal.

## 9. Time and space complexity

For N nodes, worst-case time and auxiliary space are O(N) due to parent indexing.

## 10. Why the algorithm works

There is exactly one simple path from the target to each node. Skipping the immediately preceding node prevents reversing any tree edge.

## 11. When to use it

Find every node exactly k undirected edges from a target.

## 12. When not to use it

A general graph with cycles needs a visited set instead of only the previous-node check.

## 13. Common mistakes

Search upward as well as downward and compare identities when values repeat.

## 14. Alternative approaches

An explicit stack avoids using Python call frames.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Treat parent and children as neighbors, then stop BFS branches at the desired distance. Search upward as well as downward and compare identities when values repeat.
