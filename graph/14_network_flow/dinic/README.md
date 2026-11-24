# Dinic’s Algorithm

**P3**

## 1. What is the algorithm?

Find maximum flow by handling many shortest augmenting paths per search phase.

## 2. Problem it solves

Find maximum flow by handling many shortest augmenting paths per search phase.

## 3. Core intuition

Use BFS distances to keep only arcs that advance one level, then block every route in that level graph before rebuilding layers.

## 4. Prerequisites

Graph representations and the traversal or recurrence used below.

## 5. How it works

1. Compute residual BFS levels.
2. Use depth-first flow pushes along arcs going to the next level.
3. Keep current-edge cursors and rebuild levels only after all layered routes are blocked.

## 6. Visual example

```text
s ─3→ a ─2→ t
 \2→ b ─4─↗
```

## 7. Dry run

Levels are s=0, a=b=1, t=2. One phase sends 2 through a and 2 through b. A second BFS cannot reach t.

## 8. Python implementation

Start with `dinic` in [implementation.py](implementation.py). Keep current-edge cursors and rebuild levels only after all layered routes are blocked.

Run the example from the repository root with `uv run python -m graph.14_network_flow.dinic.implementation`.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V vertices and E edges, general worst-case time is O(V²E) plus setup and auxiliary space is O(V + E). Each blocking phase costs O(VE), and the sink's level increases between successful phases.

## 10. Why the algorithm works

A blocking flow saturates an arc on every shortest residual path. Its new reverse arcs lead backward by one layer, so they cannot create a shorter or equally short path to the sink.

## 11. When to use it

Find maximum flow by handling many shortest augmenting paths per search phase.

## 12. When not to use it

Long residual paths can exceed the recursive implementation's Python recursion limit.

## 13. Common mistakes

Reset edge cursors between level graphs and require each push to advance exactly one level.

## 14. Alternative approaches

Edmonds–Karp also uses BFS, but it rebuilds the search after every augmentation.

## 15. Practice problems

**Original exercise · P3.** Modify the worked example to introduce an isolated vertex, and predict the result before running the code.

## 16. Interview revision notes

Use BFS distances to keep only arcs that advance one level, then block every route in that level graph before rebuilding layers. Reset edge cursors between level graphs and require each push to advance exactly one level.
