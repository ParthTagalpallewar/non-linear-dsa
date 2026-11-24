# Kosaraju’s Algorithm

**P2**

## 1. What is the algorithm?

Find groups of mutually reachable vertices in a directed graph.

## 2. Problem it solves

Find groups of mutually reachable vertices in a directed graph.

## 3. Core intuition

The component with the latest finish is a source in the remaining component DAG. Reverse edges to keep its search inside the component.

## 4. Prerequisites

Graph representations and the traversal or recurrence used below.

## 5. How it works

1. Build the transpose graph.
2. Record DFS exit order in the original graph.
3. In reverse exit order, traverse unseen vertices in the transpose to extract components.

## 6. Visual example

```text
0 ⇄ 1 → 2 ⇄ 3
```

## 7. Dry run

A search from 0 finishes [3, 2, 1, 0]. In the transpose a traversal from 0 reaches {0, 1}. The next unexplored vertex starts {2, 3}.

## 8. Python implementation

Start with `kosaraju` in [implementation.py](implementation.py). In reverse exit order, traverse unseen vertices in the transpose to extract components.

## 9. Time and space complexity

For V vertices and E edges, time and auxiliary space are O(V + E), including the transpose.

## 10. Why the algorithm works

Across an edge between distinct components, the maximum finish time in the predecessor exceeds that in the successor. Reversing edges prevents the latest unexplored component from reaching others.

## 11. When to use it

Find groups of mutually reachable vertices in a directed graph.

## 12. When not to use it

Very deep graphs can exceed Python's DFS recursion limit.

## 13. Common mistakes

Record finish time after exploring descendants. Reset visited state for the second pass.

## 14. Alternative approaches

Tarjan extracts components in one DFS and avoids the transpose.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example to introduce an isolated vertex, and predict the result before running the code.

## 16. Interview revision notes

The component with the latest finish is a source in the remaining component DAG. Reverse edges to keep its search inside the component. Record finish time after exploring descendants. Reset visited state for the second pass.
