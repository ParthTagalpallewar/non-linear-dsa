# A* Search

**P2**

## 1. What is the algorithm?

Find one shortest route using a lower bound on remaining cost.

## 2. Problem it solves

Find one shortest route using a lower bound on remaining cost.

## 3. Core intuition

Prioritize estimated total cost g+h, where g is known prefix cost and h underestimates the remaining cost.

## 4. Prerequisites

Adjacency or edge lists, distance arrays, and edge relaxation.

## 5. How it works

1. Push the start at priority h(start).
2. Expand the minimum current g+h and allow strict improvements to reopen vertices.
3. When the goal is popped, reconstruct the path from predecessors.

## 6. Visual example

```text
0 ─4→ 1 ─5→ 3
 \2→ 2 ─1↗
```

## 7. Dry run

In the example, 1 is first expanded at g=4. Vertex 2 later improves it to g=3, and the reopened 1 improves the goal to 8.

## 8. Python implementation

Start with `a_star` in [implementation.py](implementation.py). When the goal is popped, reconstruct the path from predecessors.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V vertices and E edges, with a consistent heuristic and O(1) evaluation, time is O(V + E log(E + 1)) and space O(V + E). An inconsistent heuristic can cause many re-expansions.

## 10. Why the algorithm works

Before an optimal goal is popped, a frontier vertex on an optimal route has g+h no greater than that route's cost. A more expensive goal cannot win the priority queue against it.

## 11. When to use it

Find one shortest route using a lower bound on remaining cost.

## 12. When not to use it

An overestimating heuristic voids the optimality guarantee.

## 13. Common mistakes

Allow reopening if consistency is not guaranteed, and require zero heuristic at the goal.

## 14. Alternative approaches

Use h=0 for Dijkstra's search order.

## 15. Practice problems

**Original exercise · P2.** Trace the algorithm with a disconnected fourth vertex and explain its final distance.

## 16. Interview revision notes

Prioritize estimated total cost g+h, where g is known prefix cost and h underestimates the remaining cost. Allow reopening if consistency is not guaranteed, and require zero heuristic at the goal.
