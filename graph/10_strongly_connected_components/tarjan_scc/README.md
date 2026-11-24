# Tarjan’s SCC Algorithm

**P2**

## 1. What is the algorithm?

Extract SCCs in one directed DFS without building a transpose.

## 2. Problem it solves

Extract SCCs in one directed DFS without building a transpose.

## 3. Core intuition

Keep undecided vertices on a stack. Low-link values tell whether a subtree can reach earlier undecided vertices.

## 4. Prerequisites

Graph representations and the traversal or recurrence used below.

## 5. How it works

1. Stamp and push each newly visited vertex.
2. Propagate child low-links and use discovery times for edges to active vertices.
3. When low equals discovery time, pop through that component root.

## 6. Visual example

```text
0 ⇄ 1 → 2 ⇄ 3
```

## 7. Dry run

Edge 3→2 lowers low[3] to entry[2], so returning from 2 pops 3 and 2. Returning from 0 later pops 1 and 0.

## 8. Python implementation

Start with `tarjan_scc` in [implementation.py](implementation.py). When low equals discovery time, pop through that component root.

Run the example from the repository root with `uv run python -m graph.10_strongly_connected_components.tarjan_scc.implementation`.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V vertices and E edges, time is O(V + E) and auxiliary space is O(V). Each vertex enters and leaves the stack once.

## 10. Why the algorithm works

A low-link smaller than a vertex's entry witnesses a route back to an earlier active vertex. At equality the component cannot extend farther down the stack and the suffix is mutually reachable.

## 11. When to use it

Extract SCCs in one directed DFS without building a transpose.

## 12. When not to use it

Very deep inputs may need an iterative DFS.

## 13. Common mistakes

Only use previously discovered endpoints if they remain on the component stack.

## 14. Alternative approaches

Kosaraju trades a second pass and transpose for simpler state.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example to introduce an isolated vertex, and predict the result before running the code.

## 16. Interview revision notes

Keep undecided vertices on a stack. Low-link values tell whether a subtree can reach earlier undecided vertices. Only use previously discovered endpoints if they remain on the component stack.
