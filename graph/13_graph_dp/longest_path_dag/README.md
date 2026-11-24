# Longest Path in a DAG

**P2**

## 1. What is the algorithm?

Find the highest-cost route from a fixed source in an acyclic graph.

## 2. Problem it solves

Find the highest-cost route from a fixed source in an acyclic graph.

## 3. Core intuition

Replace minimum with maximum in topological relaxation and use negative infinity to mark unreachable states.

## 4. Prerequisites

Graph representations and the traversal or recurrence used below.

## 5. How it works

1. Topologically order the weighted graph by destination.
2. Seed only the source with zero.
3. Maximize the current score at the destination of every edge.

## 6. Visual example

```text
0 ─(−2)→ 1 ─1→ 2
```

## 7. Dry run

From 0, the direct route to 2 scores −5. Processing 1 improves 2 to −2 + 1 = −1.

## 8. Python implementation

Start with `longest_path_dag` in [implementation.py](implementation.py). Maximize the current score at the destination of every edge.

## 9. Time and space complexity

For V vertices and E edges, time and auxiliary space are O(V + E), including the unweighted projection.

## 10. Why the algorithm works

Every path to a vertex is the source itself or extends a path through a predecessor already processed in the topological order.

## 11. When to use it

Find the highest-cost route from a fixed source in an acyclic graph.

## 12. When not to use it

General longest simple path on cyclic graphs is NP-hard.

## 13. Common mistakes

Use negative infinity rather than zero for unreachable vertices.

## 14. Alternative approaches

Negate integer weights and use DAG shortest paths to obtain the same answer.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example to introduce an isolated vertex, and predict the result before running the code.

## 16. Interview revision notes

Replace minimum with maximum in topological relaxation and use negative infinity to mark unreachable states. Use negative infinity rather than zero for unreachable vertices.
