# Subtree Queries Using an Euler Tour

**P2**

## 1. What is the algorithm?

Answer many static subtree sum queries in constant time each after preprocessing.

## 2. Problem it solves

Answer many static subtree sum queries in constant time each after preprocessing.

## 3. Core intuition

Map each subtree to a contiguous preorder interval and subtract array prefix sums.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Root the undirected tree and preprocess the indicated index.
2. Map each subtree to a contiguous preorder interval and subtract array prefix sums.
3. Return the result for each requested vertex or pair.

## 6. Visual example

```text
    0
   / \
  1   2
 / \
3   4
```

## 7. Dry run

Preorder [0, 1, 3, 4, 2] gives subtree 1 interval [1, 4), which maps to values 2, 4, 5.

## 8. Python implementation

Start with `subtree_queries` in [implementation.py](implementation.py). Return the result for each requested vertex or pair.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes and Q queries, total time O(N + Q), preprocessing space O(N), and result space O(Q).

## 10. Why the algorithm works

DFS completes all descendants before any following nonsubtree vertex. Prefix subtraction extracts exactly that interval.

## 11. When to use it

Answer many static subtree sum queries in constant time each after preprocessing.

## 12. When not to use it

The index assumes a fixed tree structure. Rebuild it after edges change.

## 13. Common mistakes

Use only the first appearance of each vertex for values to avoid counting return visits.

## 14. Alternative approaches

A Fenwick tree on preorder values handles point updates in O(log N).

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Map each subtree to a contiguous preorder interval and subtract array prefix sums. Use only the first appearance of each vertex for values to avoid counting return visits.
