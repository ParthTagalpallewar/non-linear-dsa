# Shortest Path Reconstruction

**P1**

## 1. What is the algorithm?

Return the actual route underlying a shortest-path distance.

## 2. Problem it solves

Return the actual route underlying a shortest-path distance.

## 3. Core intuition

Each successful relaxation records the predecessor that supplied the improved distance.

## 4. Prerequisites

Adjacency or edge lists, distance arrays, and edge relaxation.

## 5. How it works

1. Run Dijkstra while recording predecessors.
2. Check whether the target is reachable.
3. Walk backward from target through predecessors and reverse.

## 6. Visual example

```text
0 ─10→ 1
 \2→ 2 ─3↗
```

## 7. Dry run

Vertex 1 first gets parent 0 and later gets parent 2. Backtracking produces [1, 2, 0], which reverses to [0, 2, 1].

## 8. Python implementation

Start with `shortest_path_reconstruction` in [implementation.py](implementation.py). Walk backward from target through predecessors and reverse.

## 9. Time and space complexity

For V vertices and E edges, Dijkstra dominates at O(V + E log(E + 1)) time and O(V + E) space. Reversing a route with K vertices takes O(K).

## 10. Why the algorithm works

A recorded predecessor supplies a tight incoming edge on a shortest route. Strict relaxation and settlement order prevent parent loops.

## 11. When to use it

Return the actual route underlying a shortest-path distance.

## 12. When not to use it

One predecessor per vertex cannot enumerate all tied shortest paths.

## 13. Common mistakes

Update the predecessor when distance improves and distinguish an unreachable target from the source.

## 14. Alternative approaches

For unit edges, BFS can record predecessors in linear time.

## 15. Practice problems

**Original exercise · P1.** Trace the algorithm with a disconnected fourth vertex and explain its final distance.

## 16. Interview revision notes

Each successful relaxation records the predecessor that supplied the improved distance. Update the predecessor when distance improves and distinguish an unreachable target from the source.
