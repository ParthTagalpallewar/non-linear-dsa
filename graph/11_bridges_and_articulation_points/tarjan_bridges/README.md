# Tarjan’s Bridge Algorithm

**P2**

## 1. What is the algorithm?

Find edges whose removal disconnects a component.

## 2. Problem it solves

Find edges whose removal disconnects a component.

## 3. Core intuition

DFS low links measure whether a child subtree can escape to the parent or above.

## 4. Prerequisites

Graph representations and the traversal or recurrence used below.

## 5. How it works

1. Assign a discovery timestamp and remember the incoming edge index.
2. Propagate the minimum timestamps found through back edges and child subtrees.
3. A tree edge is a bridge if the child cannot reach even the parent's discovery time.

## 6. Visual example

```text
0 ═ 1 ─ 2 ─ 3
```

## 7. Dry run

With discovery order 0, 1, 2, 3, the second edge between 0 and 1 lowers low[1] to 0. The tail has low[2]=2 and low[3]=3.

## 8. Python implementation

Start with `tarjan_bridges` in [implementation.py](implementation.py). A tree edge is a bridge if the child cannot reach even the parent's discovery time.

## 9. Time and space complexity

For V vertices and E edges, DFS takes O(V + E) time and auxiliary space. Sorting K returned IDs adds O(K log(K + 1)) time.

## 10. Why the algorithm works

If low[child] > entry[parent], the tree edge is the only route out of the child subtree.

## 11. When to use it

Find edges whose removal disconnects a component.

## 12. When not to use it

The method is for undirected graphs. A long DFS chain can exceed Python's recursion limit.

## 13. Common mistakes

Skip only the incoming physical edge. A parallel edge back to the parent must still reduce the low value.

## 14. Alternative approaches

Removing each candidate and checking connectivity provides a simple brute-force oracle but repeats the traversal.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example to introduce an isolated vertex, and predict the result before running the code.

## 16. Interview revision notes

DFS low links measure whether a child subtree can escape to the parent or above. Skip only the incoming physical edge. A parallel edge back to the parent must still reduce the low value.
