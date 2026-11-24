# Shortest Paths in a DAG

**P1**

## 1. What is the algorithm?

Find cheapest routes in acyclic dependencies with positive or negative edge costs.

## 2. Problem it solves

Find cheapest routes in acyclic dependencies with positive or negative edge costs.

## 3. Core intuition

A topological order puts every possible predecessor before the vertex it can improve.

## 4. Prerequisites

Adjacency or edge lists, distance arrays, and edge relaxation.

## 5. How it works

1. Topologically order the graph and reject cycles.
2. Set only the source to zero.
3. Relax outgoing edges in topological order.

## 6. Visual example

```text
0 ─→ 1 ─→ 2
```

## 7. Dry run

With 0→1 costing 2 and 1→2 costing −3, the distance array becomes [0, 2, −1].

## 8. Python implementation

Start with `dag_shortest_path` in [implementation.py](implementation.py). Relax outgoing edges in topological order.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V vertices and E edges, time is O(V + E). Auxiliary space is O(V + E) because topological sorting uses a projected adjacency list.

## 10. Why the algorithm works

When a vertex is processed, all incoming edges have already been relaxed using final predecessor distances.

## 11. When to use it

Find cheapest routes in acyclic dependencies with positive or negative edge costs.

## 12. When not to use it

Graphs with directed cycles require another approach.

## 13. Common mistakes

Keep unreachable vertices at infinity even when their outgoing edges have negative weight.

## 14. Alternative approaches

Bellman–Ford supports negative edges without requiring a DAG.

## 15. Practice problems

**Original exercise · P1.** Trace the algorithm with a disconnected fourth vertex and explain its final distance.

## 16. Interview revision notes

A topological order puts every possible predecessor before the vertex it can improve. Keep unreachable vertices at infinity even when their outgoing edges have negative weight.
