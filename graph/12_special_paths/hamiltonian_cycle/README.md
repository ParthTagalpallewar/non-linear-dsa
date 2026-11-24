# Hamiltonian Cycle Using Backtracking

**P3**

## 1. What is the algorithm?

Seek a route that visits each vertex exactly once and returns to its start.

## 2. Problem it solves

Seek a route that visits each vertex exactly once and returns to its start.

## 3. Core intuition

Explore one unvisited outgoing neighbor at a time and undo any choice that cannot complete the route.

## 4. Prerequisites

Graph representations and the traversal or recurrence used below.

## 5. How it works

1. Mark the initial vertex.
2. Extend the route along an edge to an unused vertex.
3. After all vertices are included, verify the closing edge.

## 6. Visual example

```text
0 → 2 → 1
 \──────↗
```

## 7. Dry run

Trying 0→1 first gets stuck before reaching 2. Undo that choice and try 0→2→1, then close at 0.

## 8. Python implementation

Start with `hamiltonian_cycle` in [implementation.py](implementation.py). After all vertices are included, verify the closing edge.

## 9. Time and space complexity

For V vertices and maximum adjacency length D, exploring vertex permutations on a simple graph takes O(V! × (D + 1)) worst-case time and O(V) auxiliary space. Repeated adjacency entries can repeat branches.

## 10. Why the algorithm works

Each branch represents a valid simple prefix and every possible next vertex is considered. Starting at one fixed vertex suffices for a cycle because a cycle can be rotated.

## 11. When to use it

Seek a route that visits each vertex exactly once and returns to its start.

## 12. When not to use it

General Hamiltonian search becomes impractical as V grows.

## 13. Common mistakes

Undo both visited state and the route when a recursive call fails.

## 14. Alternative approaches

Bitmask dynamic programming can replace repeated suffix searches with O(V²2^V) time and O(V2^V) state on dense graphs.

## 15. Practice problems

**Original exercise · P3.** Modify the worked example to introduce an isolated vertex, and predict the result before running the code.

## 16. Interview revision notes

Explore one unvisited outgoing neighbor at a time and undo any choice that cannot complete the route. Undo both visited state and the route when a recursive call fails.
