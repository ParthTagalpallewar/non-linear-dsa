# Maximum Flow

**P2**

## 1. What is the algorithm?

Find the highest feasible transfer rate from one source to one sink.

## 2. Problem it solves

Find the highest feasible transfer rate from one source to one sink.

## 3. Core intuition

Use breadth-first search to find a path of positive residual capacity, then augment by its bottleneck.

## 4. Prerequisites

Graph representations and the traversal or recurrence used below.

## 5. How it works

1. Set all original flows to zero and build paired residual arcs.
2. Search for a breadth-first residual path to the sink.
3. Subtract the bottleneck on forward arcs, add it on reverse arcs, and repeat until no path remains.

## 6. Visual example

```text
s ─3→ a ─2→ t
 \2→ b ─4─↗
```

## 7. Dry run

Augment 2 along s→a→t and 2 along s→b→t. The remaining first branch has no usable edge to t, so flow is 4.

## 8. Python implementation

Start with `maximum_flow` in [implementation.py](implementation.py). Subtract the bottleneck on forward arcs, add it on reverse arcs, and repeat until no path remains.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V vertices and E arcs the running time is O(V E²) for the standard bound on nontrivial networks, plus O(V + E) setup. Residual storage and traversal state use O(V + E) space.

## 10. Why the algorithm works

Augmenting a path preserves capacity constraints and conservation. At termination no residual capacity crosses the reachable source-side cut outward, so the flow meets that cut's upper bound.

## 11. When to use it

Find the highest feasible transfer rate from one source to one sink.

## 12. When not to use it

This implementation assumes integral capacities and a single source and sink.

## 13. Common mistakes

Keep separate reverse arc identities, especially when parallel or antiparallel arcs occur.

## 14. Alternative approaches

Dinic processes entire level graphs. Arbitrary-path Ford–Fulkerson can use more augmentations than shortest-path Edmonds–Karp.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example to introduce an isolated vertex, and predict the result before running the code.

## 16. Interview revision notes

Use breadth-first search to find a path of positive residual capacity, then augment by its bottleneck. Keep separate reverse arc identities, especially when parallel or antiparallel arcs occur.
