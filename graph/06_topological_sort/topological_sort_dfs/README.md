# Topological Sort Using DFS

**P1**

## 1. What is the algorithm?

Topological Sort Using DFS answers a structural question about a graph.

## 2. Problem it solves

Order dependencies ahead of consumers.

## 3. Core intuition

Append vertices when their outgoing DFS scans finish, then reverse the result.

## 4. Prerequisites

Adjacency lists, vertex indexing, and the traversal used by the implementation.

## 5. How it works

1. Initialize per-vertex state.
2. Append vertices when their outgoing DFS scans finish, then reverse the result.
3. Use the final state to produce the result.

## 6. Visual example

```text
0 → 1 → 2
```

## 7. Dry run

For 0→1→2 the finish list is [2, 1, 0], so the answer is [0, 1, 2].

## 8. Python implementation

Start with `topological_sort_dfs` in [implementation.py](implementation.py). Use the final state to produce the result.

## 9. Time and space complexity

For V vertices and E edges, time is O(V + E) and auxiliary space is O(V). Each vertex is scheduled once and its adjacency is scanned once.

## 10. Why the algorithm works

For each edge u→v in a DAG, v finishes before u, because v is either explored recursively from u or already finished.

## 11. When to use it

Order dependencies ahead of consumers.

## 12. When not to use it

Deep dependency graphs may exceed Python's recursion limit.

## 13. Common mistakes

Track active vertices and reject back edges before trusting the order.

## 14. Alternative approaches

Compare the search state with the other implementations in this topic.

## 15. Practice problems

**Original exercise · P1.** Modify the example to include an isolated vertex and predict how the result changes.

## 16. Interview revision notes

Append vertices when their outgoing DFS scans finish, then reverse the result. Track active vertices and reject back edges before trusting the order.
