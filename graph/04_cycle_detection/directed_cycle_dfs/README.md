# Directed Cycle Detection Using DFS

**P1**

## 1. What is the algorithm?

Directed Cycle Detection Using DFS answers a structural question about a graph.

## 2. Problem it solves

Determine whether directed dependencies are circular.

## 3. Core intuition

Distinguish unseen vertices, active recursion frames, and finished vertices.

## 4. Prerequisites

Adjacency lists, vertex indexing, and the traversal used by the implementation.

## 5. How it works

1. Initialize per-vertex state.
2. Distinguish unseen vertices, active recursion frames, and finished vertices.
3. Use the final state to produce the result.

## 6. Visual example

```text
0 → 1 ⇄ 2
```

## 7. Dry run

In 0→1→2→1, visiting 2 finds state 1 at vertex 1, which is still active.

## 8. Python implementation

Start with `directed_cycle_dfs` in [implementation.py](implementation.py). Use the final state to produce the result.

## 9. Time and space complexity

For V vertices and E edges, time is O(V + E) and auxiliary space is O(V). Each vertex is scheduled once and its adjacency is scanned once.

## 10. Why the algorithm works

Active vertices form the current directed DFS path. An edge back along that path closes a cycle. Traversing any directed cycle must find an active vertex before all its members finish.

## 11. When to use it

Determine whether directed dependencies are circular.

## 12. When not to use it

Use Kahn's algorithm or an explicit stack if depth can exceed Python's recursion limit.

## 13. Common mistakes

A previously finished neighbor can be reached by multiple branches in a DAG.

## 14. Alternative approaches

Compare the search state with the other implementations in this topic.

## 15. Practice problems

**Original exercise · P1.** Modify the example to include an isolated vertex and predict how the result changes.

## 16. Interview revision notes

Distinguish unseen vertices, active recursion frames, and finished vertices. A previously finished neighbor can be reached by multiple branches in a DAG.
