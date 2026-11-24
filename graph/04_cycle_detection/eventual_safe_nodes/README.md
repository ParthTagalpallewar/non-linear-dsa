# Eventual Safe Nodes

**P1**

## 1. What is the algorithm?

Eventual Safe Nodes answers a structural question about a graph.

## 2. Problem it solves

Find starting states from which all transitions eventually stop.

## 3. Core intuition

Reverse the graph and eliminate vertices whose original outgoing choices are all known safe.

## 4. Prerequisites

Adjacency lists, vertex indexing, and the traversal used by the implementation.

## 5. How it works

1. Initialize per-vertex state.
2. Reverse the graph and eliminate vertices whose original outgoing choices are all known safe.
3. Use the final state to produce the result.

## 6. Visual example

```text
1 ↺ ← 0 → 2 → 3
```

## 7. Dry run

Vertex 3 is terminal and becomes safe first. Then 2 becomes safe. Vertex 0 still has a choice leading to the loop at 1.

## 8. Python implementation

Start with `eventual_safe_nodes` in [implementation.py](implementation.py). Use the final state to produce the result.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V vertices and E edges, time and auxiliary space are O(V + E) because we build and traverse the reverse graph.

## 10. Why the algorithm works

A vertex is safe exactly when all of its successors are safe. The residual graph has at least one residual outgoing edge per vertex, so a walk can continue until it repeats.

## 11. When to use it

Find starting states from which all transitions eventually stop.

## 12. When not to use it

The graph must use integer vertex IDs from 0 to V−1.

## 13. Common mistakes

One route to a terminal is insufficient when another route reaches a cycle.

## 14. Alternative approaches

Compare the search state with the other implementations in this topic.

## 15. Practice problems

- LeetCode #802, Medium. Reverse edge elimination from terminal states. [Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/)

**Original exercise · P1.** Modify the example to include an isolated vertex and predict how the result changes.

## 16. Interview revision notes

Reverse the graph and eliminate vertices whose original outgoing choices are all known safe. One route to a terminal is insufficient when another route reaches a cycle.
