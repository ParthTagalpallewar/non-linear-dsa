# Johnson’s All-Pairs Shortest Paths

**P3**

## 1. What is the algorithm?

Compute all-pairs distances on a sparse graph that permits negative edges.

## 2. Problem it solves

Compute all-pairs distances on a sparse graph that permits negative edges.

## 3. Core intuition

Shortest distances from a super-source provide potentials that turn every original edge nonnegative.

## 4. Prerequisites

Adjacency or edge lists, distance arrays, and edge relaxation.

## 5. How it works

1. Use Bellman–Ford from an extra zero-edge source.
2. Replace w(u,v) by w(u,v)+h(u)−h(v).
3. Run Dijkstra from every original vertex and reverse the potential shift.

## 6. Visual example

```text
0 ─2→ 1 ─(−5)→ 2
 \─────3────────↗
```

## 7. Dry run

The super-source gives h=[0, 0, −5] for the example. The edge 1→2 goes from −5 to 0. The new path from 0 to 2 costs 2, which converts back to −3.

## 8. Python implementation

Start with `johnson` in [implementation.py](implementation.py). Run Dijkstra from every original vertex and reverse the potential shift.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V vertices and E edges, time is O(V² + VE log(E + 1)) with lazy heaps. The result stores O(V²) distances and working space is O(V + E).

## 10. Why the algorithm works

Bellman–Ford makes h(v)≤h(u)+w(u,v), guaranteeing nonnegative reweights. All internal potential terms cancel, so every route from u to v receives exactly the same shift.

## 11. When to use it

Compute all-pairs distances on a sparse graph that permits negative edges.

## 12. When not to use it

Floyd–Warshall can be simpler and faster for dense graphs.

## 13. Common mistakes

Use a super-source so Bellman–Ford can find negative cycles in any component. Restore the correct potential signs.

## 14. Alternative approaches

Use Floyd–Warshall for a compact dynamic program without heaps.

## 15. Practice problems

**Original exercise · P3.** Trace the algorithm with a disconnected fourth vertex and explain its final distance.

## 16. Interview revision notes

Shortest distances from a super-source provide potentials that turn every original edge nonnegative. Use a super-source so Bellman–Ford can find negative cycles in any component. Restore the correct potential signs.
