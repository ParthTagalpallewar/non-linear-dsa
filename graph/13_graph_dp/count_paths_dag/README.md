# Counting Paths in a DAG

**P2**

## 1. What is the algorithm?

Count routes from one start without enumerating them.

## 2. Problem it solves

Count routes from one start without enumerating them.

## 3. Core intuition

Sum the number of prefixes separately for each possible final edge.

## 4. Prerequisites

Graph representations and the traversal or recurrence used below.

## 5. How it works

1. Seed the source with its one empty walk.
2. Process vertices in topological order.
3. Add each vertex's count once per outgoing edge.

## 6. Visual example

```text
0 → 1 → 3
 \→ 2 ↗
```

## 7. Dry run

After 0, counts are [1, 1, 1, 0]. Edges from 1 and 2 raise the count at 3 to 2.

## 8. Python implementation

Start with `count_paths_dag` in [implementation.py](implementation.py). Add each vertex's count once per outgoing edge.

## 9. Time and space complexity

For V vertices and E edges, there are O(V + E) operations and O(V) stored counts. Python large-integer addition can add bit complexity as counts grow.

## 10. Why the algorithm works

Each nonempty path has a unique final physical edge and prefix. Summing those disjoint choices counts every route once.

## 11. When to use it

Count routes from one start without enumerating them.

## 12. When not to use it

A reachable cycle makes the number of walks unbounded along some routes.

## 13. Common mistakes

Decide whether parallel edges should be distinct routes.

## 14. Alternative approaches

Recursive memoization computes counts from incoming edges on demand.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example to introduce an isolated vertex, and predict the result before running the code.

## 16. Interview revision notes

Sum the number of prefixes separately for each possible final edge. Decide whether parallel edges should be distinct routes.
