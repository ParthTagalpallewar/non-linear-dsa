# Edge List

**P1**

## 1. What is the algorithm?

An edge list stores one row per edge, optionally with a weight.

## 2. Problem it solves

Scan or sort all edges for algorithms such as Bellman–Ford and Kruskal.

## 3. Core intuition

Storing each input record once makes whole-edge scans straightforward.

## 4. Prerequisites

Tuples, vertex labels, and weighted edges.

## 5. How it works

1. Validate the vertex count.
2. Read each edge and validate both endpoints.
3. Append the original orientation and weight.

## 6. Visual example

```text
0 --(-2)--> 1    2
```

## 7. Dry run

For three vertices and one edge, the list becomes [(0, 1, -2)]. Vertex 2 remains implicit.

## 8. Python implementation

Start with `edge_list` in [implementation.py](implementation.py). Append the original orientation and weight.

## 9. Time and space complexity

For E edges, build time and output space are O(E), with O(1) auxiliary space. Finding all neighbors of a vertex costs O(E).

## 10. Why the algorithm works

After processing k inputs, the result has exactly those k validated records in input order.

## 11. When to use it

Scan or sort all edges for algorithms such as Bellman–Ford and Kruskal.

## 12. When not to use it

Repeated neighbor lookups benefit from an adjacency index.

## 13. Common mistakes

Retain the vertex count separately because isolated vertices have no edge records.

## 14. Alternative approaches

Build adjacency lists in O(V + E) when the workload follows incident edges frequently.

## 15. Practice problems

**Original exercise · P1.** Sort the records by weight while retaining parallel edges.

## 16. Interview revision notes

Storing each input record once makes whole-edge scans straightforward. Retain the vertex count separately because isolated vertices have no edge records.
