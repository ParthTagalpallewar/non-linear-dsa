# Kahn’s Algorithm

**P1**

## 1. What is the algorithm?

Kahn’s Algorithm answers a structural question about a graph.

## 2. Problem it solves

Return a dependency order and detect cycles iteratively.

## 3. Core intuition

Queue vertices when their remaining indegree reaches zero.

## 4. Prerequisites

Adjacency lists, vertex indexing, and the traversal used by the implementation.

## 5. How it works

1. Initialize per-vertex state.
2. Queue vertices when their remaining indegree reaches zero.
3. Use the final state to produce the result.

## 6. Visual example

```text
0 → 1 → 2
```

## 7. Dry run

For 0→1→2, the queue evolves [0], [1], [2], and then empty.

## 8. Python implementation

Start with `kahn` in [implementation.py](implementation.py). Use the final state to produce the result.

Run the example from the repository root with `uv run python -m graph.06_topological_sort.kahn.implementation`.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V vertices and E edges, time is O(V + E) and auxiliary space is O(V). Each vertex is scheduled once and its adjacency is scanned once.

## 10. Why the algorithm works

Queued vertices have no unmet predecessors. Removing them preserves that invariant and eventually empties every finite DAG.

## 11. When to use it

Return a dependency order and detect cycles iteratively.

## 12. When not to use it

The graph must use integer vertex IDs from 0 to V−1.

## 13. Common mistakes

Count and decrement each parallel edge consistently.

## 14. Alternative approaches

Compare the search state with the other implementations in this topic.

## 15. Practice problems

- LeetCode #210, Medium. Indegree-based ordering and cycle detection. [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

**Original exercise · P1.** Modify the example to include an isolated vertex and predict how the result changes.

## 16. Interview revision notes

Queue vertices when their remaining indegree reaches zero. Count and decrement each parallel edge consistently.
