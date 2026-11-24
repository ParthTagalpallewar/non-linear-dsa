# Unweighted Shortest Paths Using BFS

**P1**

## 1. What is the algorithm?

Measure the fewest edges from one source to each reachable vertex.

## 2. Problem it solves

Measure the fewest edges from one source to each reachable vertex.

## 3. Core intuition

FIFO discovery visits vertices in increasing distance layers.

## 4. Prerequisites

Adjacency or edge lists, distance arrays, and edge relaxation.

## 5. How it works

1. Assign zero to the source and infinity elsewhere.
2. Queue the source.
3. Assign distance one more than the current vertex to each unseen neighbor.

## 6. Visual example

```text
0 ─→ 1 ─→ 2
```

## 7. Dry run

Starting at 0 gives distance 0. Processing 0 discovers 1 at distance 1. Processing 1 discovers 2 at distance 2.

## 8. Python implementation

Start with `unweighted_bfs` in [implementation.py](implementation.py). Assign distance one more than the current vertex to each unseen neighbor.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V vertices and E adjacency entries, time is O(V + E), with O(V) space for distances and the queue.

## 10. Why the algorithm works

Any shorter path would reach the vertex from an earlier layer that has already been expanded.

## 11. When to use it

Measure the fewest edges from one source to each reachable vertex.

## 12. When not to use it

Edges with different costs need weighted shortest paths.

## 13. Common mistakes

Mark on enqueue so each vertex enters the queue once.

## 14. Alternative approaches

Dijkstra specializes to this layer order when all edges cost one.

## 15. Practice problems

**Original exercise · P1.** Trace the algorithm with a disconnected fourth vertex and explain its final distance.

## 16. Interview revision notes

FIFO discovery visits vertices in increasing distance layers. Mark on enqueue so each vertex enters the queue once.
