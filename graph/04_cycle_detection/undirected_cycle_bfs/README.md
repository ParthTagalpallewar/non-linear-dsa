# Undirected Cycle Detection Using BFS

**P1**

## 1. What is the algorithm?

Undirected Cycle Detection Using BFS answers a structural question about a graph.

## 2. Problem it solves

Detect a redundant route in an undirected graph.

## 3. Core intuition

Expand discovered vertices and ignore exactly one reverse parent edge per vertex.

## 4. Prerequisites

Adjacency lists, vertex indexing, and the traversal used by the implementation.

## 5. How it works

1. Initialize per-vertex state.
2. Expand discovered vertices and ignore exactly one reverse parent edge per vertex.
3. Use the final state to produce the result.

## 6. Visual example

```text
0 ═ 1    2
```

## 7. Dry run

After 0 discovers 1, 1 skips its edge back to 0. A second such edge closes a two-edge cycle.

## 8. Python implementation

Start with `undirected_cycle_bfs` in [implementation.py](implementation.py). Use the final state to produce the result.

## 9. Time and space complexity

For V vertices and E edges, time is O(V + E) and auxiliary space is O(V). Each vertex is scheduled once and its adjacency is scanned once.

## 10. Why the algorithm works

Discovery edges form a forest. Every additional undirected edge between discovered vertices closes a cycle with that forest.

## 11. When to use it

Detect a redundant route in an undirected graph.

## 12. When not to use it

The graph must use integer vertex IDs from 0 to V−1.

## 13. Common mistakes

Skipping every edge to the parent misses parallel-edge cycles.

## 14. Alternative approaches

Compare the search state with the other implementations in this topic.

## 15. Practice problems

**Original exercise · P1.** Modify the example to include an isolated vertex and predict how the result changes.

## 16. Interview revision notes

Expand discovered vertices and ignore exactly one reverse parent edge per vertex. Skipping every edge to the parent misses parallel-edge cycles.
