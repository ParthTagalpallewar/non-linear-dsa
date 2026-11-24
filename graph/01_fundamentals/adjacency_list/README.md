# Adjacency List

**P1**

## 1. What is the algorithm?

An adjacency list associates each vertex with its outgoing neighbors.

## 2. Problem it solves

Enumerate neighbors quickly in a sparse graph.

## 3. Core intuition

Index the edges by their source so traversal can skip unrelated edges.

## 4. Prerequisites

Integer vertex labels, lists, directed and undirected edges.

## 5. How it works

1. Allocate V empty lists.
2. Append each target to its source list.
3. Insert a reverse entry for each undirected edge.

## 6. Visual example

```text
0 — 1    2
```

## 7. Dry run

Starting with [[], [], []], edge (0, 1) gives [[1], [0], []].

## 8. Python implementation

Start with `adjacency_list` in [implementation.py](implementation.py). Insert a reverse entry for each undirected edge.

Run the example from the repository root with `uv run python -m graph.01_fundamentals.adjacency_list.implementation`.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

V vertices and E input edges take O(V + E) build time and result space, with O(1) auxiliary space. Reading all neighbors of u costs O(degree(u)).

## 10. Why the algorithm works

Each edge supplies an outgoing entry at its source and, for an undirected edge, the reverse entry at its target.

## 11. When to use it

Enumerate neighbors quickly in a sparse graph.

## 12. When not to use it

Frequent arbitrary edge-membership queries can scan a long neighbor list.

## 13. Common mistakes

Allocate an independent list for every vertex and retain isolated vertices.

## 14. Alternative approaches

Use a Boolean matrix for O(1) membership or neighbor sets for expected O(1) membership with hashing.

## 15. Practice problems

**Original exercise · P1.** Build a weighted adjacency list that preserves zero-weight and parallel edges.

## 16. Interview revision notes

Index the edges by their source so traversal can skip unrelated edges. Allocate an independent list for every vertex and retain isolated vertices.
