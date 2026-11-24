# Directed Cycle Detection Using Kahn’s Algorithm

**P1**

## 1. What is the algorithm?

Directed Cycle Detection Using Kahn’s Algorithm answers a structural question about a graph.

## 2. Problem it solves

Detect a directed cycle without a recursion stack.

## 3. Core intuition

Repeatedly remove zero-indegree vertices and test whether the residual graph is empty.

## 4. Prerequisites

Adjacency lists, vertex indexing, and the traversal used by the implementation.

## 5. How it works

1. Initialize per-vertex state.
2. Repeatedly remove zero-indegree vertices and test whether the residual graph is empty.
3. Use the final state to produce the result.

## 6. Visual example

```text
0 → 1 ⇄ 2
```

## 7. Dry run

In 0→1⇄2, only 0 enters the queue. The other two retain incoming edges.

## 8. Python implementation

Start with `directed_cycle_kahn` in [implementation.py](implementation.py). Use the final state to produce the result.

## 9. Time and space complexity

For V vertices and E edges, time is O(V + E) and auxiliary space is O(V). Each vertex is scheduled once and its adjacency is scanned once.

## 10. Why the algorithm works

Every finite nonempty DAG has a zero-indegree vertex. A cycle retains its incoming cycle edges throughout elimination.

## 11. When to use it

Detect a directed cycle without a recursion stack.

## 12. When not to use it

The graph must use integer vertex IDs from 0 to V−1.

## 13. Common mistakes

A residual vertex may be downstream from a cycle without belonging to one.

## 14. Alternative approaches

Compare the search state with the other implementations in this topic.

## 15. Practice problems

**Original exercise · P1.** Modify the example to include an isolated vertex and predict how the result changes.

## 16. Interview revision notes

Repeatedly remove zero-indegree vertices and test whether the residual graph is empty. A residual vertex may be downstream from a cycle without belonging to one.
