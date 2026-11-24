# Bipartite Check Using BFS

**P1**

## 1. What is the algorithm?

Bipartite Check Using BFS answers a structural question about a graph.

## 2. Problem it solves

Separate incompatible items into two groups.

## 3. Core intuition

Propagate opposite colors while exploring with a queue.

## 4. Prerequisites

Adjacency lists, vertex indexing, and the traversal used by the implementation.

## 5. How it works

1. Initialize per-vertex state.
2. Propagate opposite colors while exploring with a queue.
3. Use the final state to produce the result.

## 6. Visual example

```text
0 — 1
 \ /
  2
```

## 7. Dry run

For a triangle with 0 colored white, both 1 and 2 must be black. Their shared edge is a contradiction.

## 8. Python implementation

Start with `bipartite_bfs` in [implementation.py](implementation.py). Use the final state to produce the result.

## 9. Time and space complexity

For V vertices and E edges, time is O(V + E) and auxiliary space is O(V). Each vertex is scheduled once and its adjacency is scanned once.

## 10. Why the algorithm works

The starting color is arbitrary. Each reachable vertex's color is forced by the parity of its discovery path. A conflict rules out either starting color.

## 11. When to use it

Separate incompatible items into two groups.

## 12. When not to use it

The graph must use integer vertex IDs from 0 to V−1.

## 13. Common mistakes

Restart at every uncolored vertex and reject self-loops.

## 14. Alternative approaches

Compare the search state with the other implementations in this topic.

## 15. Practice problems

**Original exercise · P1.** Modify the example to include an isolated vertex and predict how the result changes.

## 16. Interview revision notes

Propagate opposite colors while exploring with a queue. Restart at every uncolored vertex and reject self-loops.
