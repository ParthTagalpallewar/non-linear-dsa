# Centroid Decomposition

**P3**

## 1. What is the algorithm?

Split a tree into balanced components around a hierarchy of separators.

## 2. Problem it solves

Split a tree into balanced components around a hierarchy of separators.

## 3. Core intuition

A centroid leaves no component larger than half after removal.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Root each active component locally and count subtree sizes.
2. Choose a node whose largest child or parent-side component is at most half.
3. Remove it and process each surviving component with this centroid as its decomposition parent.

## 6. Visual example

```text
    0
   / \
  1   2
 / \
3   4
```

## 7. Dry run

For the pictured tree, removing node 1 leaves component {0,2} and singleton components {3} and {4}. No component exceeds half of five.

## 8. Python implementation

Start with `centroid_decomposition` in [implementation.py](implementation.py). Remove it and process each surviving component with this centroid as its decomposition parent.

## 9. Time and space complexity

For N vertices, each vertex and edge is inspected O(log(N + 1)) times across decomposition levels, giving O(N log(N + 1)) time and O(N) space.

## 10. Why the algorithm works

If a node has a component larger than half, moving into it reduces the largest offending side and cannot reverse back. A centroid exists, and halving bounds the recursion depth.

## 11. When to use it

Split a tree into balanced components around a hierarchy of separators.

## 12. When not to use it

Use these routines on undirected trees with symmetric adjacency and integer IDs 0 through N−1.

## 13. Common mistakes

Include the complement of a node's local subtree in the balance test.

## 14. Alternative approaches

Heavy-light decomposition optimizes one-dimensional path aggregation. Centroid decomposition is useful for distance queries split at a balanced separator.

## 15. Practice problems

**Original exercise · P3.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

A centroid leaves no component larger than half after removal. Include the complement of a node's local subtree in the balance test.
