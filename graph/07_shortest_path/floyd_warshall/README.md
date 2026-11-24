# Floyd–Warshall

**P2**

## 1. What is the algorithm?

Find shortest distances for every ordered pair, including negative edges.

## 2. Problem it solves

Find shortest distances for every ordered pair, including negative edges.

## 3. Core intuition

Allow one additional intermediate vertex at a time and compare routes that use it.

## 4. Prerequisites

Adjacency or edge lists, distance arrays, and edge relaxation.

## 5. How it works

1. Initialize diagonal zeroes and cheapest direct edges.
2. Place the allowed intermediate vertex in the outer loop.
3. Reject any negative diagonal after the updates.

## 6. Visual example

```text
0 ─2→ 1 ─(−3)→ 2
```

## 7. Dry run

After allowing intermediate 1, the route from 0 to 2 improves from infinity to 2 + (−3) = −1.

## 8. Python implementation

Start with `floyd_warshall` in [implementation.py](implementation.py). Reject any negative diagonal after the updates.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V vertices and E edges, time is O(V³ + E). The distance matrix uses O(V²) result space and the update uses O(1) additional space.

## 10. Why the algorithm works

At stage k, an optimum either bypasses k or splits into two subpaths whose intermediates come from earlier stages.

## 11. When to use it

Find shortest distances for every ordered pair, including negative edges.

## 12. When not to use it

A quadratic matrix is impractical for large sparse graphs.

## 13. Common mistakes

Keep the intermediate vertex outermost and preserve the cheapest parallel edge.

## 14. Alternative approaches

Johnson reweights once and runs heap Dijkstra from each start to exploit sparse edges.

## 15. Practice problems

**Original exercise · P2.** Trace the algorithm with a disconnected fourth vertex and explain its final distance.

## 16. Interview revision notes

Allow one additional intermediate vertex at a time and compare routes that use it. Keep the intermediate vertex outermost and preserve the cheapest parallel edge.
