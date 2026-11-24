# Undirected Cycle Detection Using DSU

**P1**

## 1. What is the algorithm?

Undirected Cycle Detection Using DSU answers a structural question about a graph.

## 2. Problem it solves

Detect redundancy while processing undirected edges.

## 3. Core intuition

Merge endpoints unless an earlier path already connects them.

## 4. Prerequisites

Adjacency lists, vertex indexing, and the traversal used by the implementation.

## 5. How it works

1. Initialize per-vertex state.
2. Merge endpoints unless an earlier path already connects them.
3. Use the final state to produce the result.

## 6. Visual example

```text
0 — 1 — 2
 \_______/
```

## 7. Dry run

Unions (0, 1) and (1, 2) succeed. Union (2, 0) sees the same representative and reports a cycle.

## 8. Python implementation

Start with `undirected_cycle_dsu` in [implementation.py](implementation.py). Use the final state to produce the result.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V vertices and E edges, initialization costs O(V), edge processing costs O(E α(V)) amortized, and auxiliary space is O(V).

## 10. Why the algorithm works

The sets equal the components formed by all earlier edges. Adding an edge within one component closes a cycle.

## 11. When to use it

Detect redundancy while processing undirected edges.

## 12. When not to use it

The graph must use integer vertex IDs from 0 to V−1.

## 13. Common mistakes

Submit each physical undirected edge once, since reverse adjacency entries duplicate it.

## 14. Alternative approaches

Compare the search state with the other implementations in this topic.

## 15. Practice problems

**Original exercise · P1.** Modify the example to include an isolated vertex and predict how the result changes.

## 16. Interview revision notes

Merge endpoints unless an earlier path already connects them. Submit each physical undirected edge once, since reverse adjacency entries duplicate it.
