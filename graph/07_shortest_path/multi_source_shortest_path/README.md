# Multi-Source Weighted Shortest Paths

**P2**

## 1. What is the algorithm?

Measure the cheapest route from any facility or origin to each vertex.

## 2. Problem it solves

Measure the cheapest route from any facility or origin to each vertex.

## 3. Core intuition

Seeding every source at zero is equivalent to adding a virtual source with zero-cost edges to all of them.

## 4. Prerequisites

Adjacency or edge lists, distance arrays, and edge relaxation.

## 5. How it works

1. Set all distinct sources to zero.
2. Put the sources in the heap.
3. Apply minimum-distance relaxation until the heap empties.

## 6. Visual example

```text
0 ─8→ 2 ←4─ 1
```

## 7. Dry run

Sources 0 and 1 start at zero. Vertex 0 proposes 8 for vertex 2, then vertex 1 improves it to 4.

## 8. Python implementation

Start with `multi_source_shortest_path` in [implementation.py](implementation.py). Apply minimum-distance relaxation until the heap empties.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For S input source entries, V vertices and E edges, time is O(S + (V + E) log(V + E + 1)) and auxiliary space is O(V + E).

## 10. Why the algorithm works

Every path from the virtual source corresponds to a path from a real source of the same cost, so ordinary Dijkstra gives the desired minima.

## 11. When to use it

Measure the cheapest route from any facility or origin to each vertex.

## 12. When not to use it

Negative weights require a different shortest-path routine.

## 13. Common mistakes

On a directed graph, reverse edges if the question asks for distances toward the facilities.

## 14. Alternative approaches

Use multi-source BFS when every edge costs one.

## 15. Practice problems

**Original exercise · P2.** Trace the algorithm with a disconnected fourth vertex and explain its final distance.

## 16. Interview revision notes

Seeding every source at zero is equivalent to adding a virtual source with zero-cost edges to all of them. On a directed graph, reverse edges if the question asks for distances toward the facilities.
