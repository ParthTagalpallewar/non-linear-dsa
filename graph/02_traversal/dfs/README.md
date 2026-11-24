# Recursive Depth-First Search

**P1**

## 1. What is the algorithm?

Recursive DFS visits a neighbor and finishes its search before trying the next neighbor.

## 2. Problem it solves

Explore reachability and build a discovery tree useful for graph analysis.

## 3. Core intuition

The call stack remembers where to resume each vertex's neighbor loop.

## 4. Prerequisites

Recursion, adjacency lists, and visited sets.

## 5. How it works

1. Mark and record the current vertex.
2. Recursively visit each unseen neighbor in input order.
3. Resume the current loop after each child returns.

## 6. Visual example

```text
0 → 1 → 3
 \→ 2 ↗
```

## 7. Dry run

The call stack grows from [0] to [0, 1, 3], unwinds to [0], then explores 2.

## 8. Python implementation

Start with `dfs` in [implementation.py](implementation.py). Resume the current loop after each child returns.

## 9. Time and space complexity

For V reachable vertices and E outgoing edges inspected, time is O(V + E) and auxiliary space is O(V).

## 10. Why the algorithm works

Each discovered vertex eventually checks every outgoing edge. An undiscovered reachable vertex would require an ignored edge from a discovered vertex.

## 11. When to use it

Explore reachability and build a discovery tree useful for graph analysis.

## 12. When not to use it

Deep graphs can exceed Python's recursion limit.

## 13. Common mistakes

Mark before calling recursively or a back edge can revisit an active frame.

## 14. Alternative approaches

Explicit stacks remove Python's recursion limit while storing equivalent frame state.

## 15. Practice problems

**Original exercise · P1.** Record each vertex's finish time as well as its entry time.

## 16. Interview revision notes

The call stack remembers where to resume each vertex's neighbor loop. Mark before calling recursively or a back edge can revisit an active frame.
