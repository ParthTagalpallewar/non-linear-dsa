# Adjacency Matrix

**P1**

## 1. What is the algorithm?

An adjacency matrix records the presence of an edge in each ordered pair's cell.

## 2. Problem it solves

Answer whether a particular pair is adjacent in constant time.

## 3. Core intuition

The source and target indices locate the edge directly.

## 4. Prerequisites

Two-dimensional lists and directed edges.

## 5. How it works

1. Allocate a square matrix of false values.
2. Mark input edges true.
3. Mark the transposed cell for undirected edges.

## 6. Visual example

```text
     0  1
  0  .  x
  1  .  .
```

## 7. Dry run

For 0→1, row 0 changes from [False, False] to [False, True]. Row 1 stays false.

## 8. Python implementation

Start with `adjacency_matrix` in [implementation.py](implementation.py). Mark the transposed cell for undirected edges.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

V vertices and E edges take O(V² + E) build time and O(V²) output space with O(1) auxiliary space. An edge query is O(1) and a neighbor scan is O(V).

## 10. Why the algorithm works

Cells start false and become true exactly when their ordered pair is supplied by an edge.

## 11. When to use it

Answer whether a particular pair is adjacent in constant time.

## 12. When not to use it

Sparse graphs with many vertices pay for cells they never use.

## 13. Common mistakes

Allocate independent rows. Boolean cells collapse parallel edges.

## 14. Alternative approaches

Neighbor sets also support expected O(1) membership while storing only present edges.

## 15. Practice problems

**Original exercise · P1.** Count incoming edges of every vertex by reading the columns.

## 16. Interview revision notes

The source and target indices locate the edge directly. Allocate independent rows. Boolean cells collapse parallel edges.
