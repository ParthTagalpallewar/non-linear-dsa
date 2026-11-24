# Breadth-First Search

**P1**

## 1. What is the algorithm?

BFS explores all vertices one edge away before exploring vertices two edges away.

## 2. Problem it solves

Find the reachable region or the fewest moves when each move costs the same.

## 3. Core intuition

A FIFO queue processes newly discovered vertices in distance order.

## 4. Prerequisites

Adjacency lists, sets, and FIFO queues.

## 5. How it works

1. Enqueue and mark the starting vertex.
2. Pop the oldest vertex and inspect its edges.
3. Mark each unseen neighbor before adding it to the queue.

## 6. Visual example

```text
0 → 1 → 3
 \→ 2 ↗
```

## 7. Dry run

| Processed | Queue afterwards |
| --- | --- |
| 0 | 1, 2 |
| 1 | 2, 3 |
| 2 | 3 |
| 3 | empty |

## 8. Python implementation

Start with `bfs` in [implementation.py](implementation.py). Mark each unseen neighbor before adding it to the queue.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V reachable vertices and E outgoing edges inspected, time is O(V + E) and auxiliary space is O(V).

## 10. Why the algorithm works

When a vertex leaves the queue, every earlier distance layer has been processed. All newly discovered neighbors are exactly one edge farther away.

## 11. When to use it

Find the reachable region or the fewest moves when each move costs the same.

## 12. When not to use it

Unequal edge weights can make the fewest-edge route more expensive.

## 13. Common mistakes

Mark vertices when enqueued to prevent duplicate queue entries.

## 14. Alternative approaches

Dijkstra handles unequal nonnegative weights. DFS is enough when only reachability matters.

## 15. Practice problems

**Original exercise · P1.** Extend BFS to return the first predecessor of each vertex.

## 16. Interview revision notes

A FIFO queue processes newly discovered vertices in distance order. Mark vertices when enqueued to prevent duplicate queue entries.
