# Eulerian Circuit

**P2**

## 1. What is the algorithm?

Use every undirected edge exactly once and finish at the start.

## 2. Problem it solves

Use every undirected edge exactly once and finish at the start.

## 3. Core intuition

Track edges by identity and collect completed portions of the walk in reverse as the stack backtracks.

## 4. Prerequisites

Graph representations and the traversal or recurrence used below.

## 5. How it works

1. Require zero odd-degree vertices.
2. Push neighbors reached through unused edges. Pop vertices with no remaining edges into the output.
3. Reverse the output and confirm that every input edge was used.

## 6. Visual example

```text
0 ═ 1 ↺
```

## 7. Dry run

The two edges between 0 and 1 and the loop at 1 produce [0, 1, 1, 0]. The isolated vertices require no visits.

## 8. Python implementation

Start with `eulerian_circuit` in [implementation.py](implementation.py). Reverse the output and confirm that every input edge was used.

## 9. Time and space complexity

For V vertices and E edges, time and auxiliary space are O(V + E). Each physical edge produces two adjacency entries and one stack push.

## 10. Why the algorithm works

Even degree pairs entrances with exits except at the two permitted endpoints. A backtracked vertex has exhausted its incident edges, so reversing the pop order splices completed cycles into the main walk.

## 11. When to use it

Use every undirected edge exactly once and finish at the start.

## 12. When not to use it

For a directed graph, apply directed degree rules and outgoing adjacency instead.

## 13. Common mistakes

Count a loop twice toward degree but consume it once, and check edge coverage for disconnected inputs.

## 14. Alternative approaches

Fleury explicitly avoids residual bridges, which gives an intuitive but slower construction.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example to introduce an isolated vertex, and predict the result before running the code.

## 16. Interview revision notes

Track edges by identity and collect completed portions of the walk in reverse as the stack backtracks. Count a loop twice toward degree but consume it once, and check edge coverage for disconnected inputs.
