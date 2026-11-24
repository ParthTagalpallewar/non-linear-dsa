# Ancestor and Descendant Queries

**P1**

## 1. What is the algorithm?

Answer a batch of ancestry queries in constant time each after preprocessing.

## 2. Problem it solves

Answer a batch of ancestry queries in constant time each after preprocessing.

## 3. Core intuition

Record the preorder interval covered by each subtree.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. Record the preorder interval covered by each subtree.
3. Produce the result from the completed traversal.

## 6. Visual example

```text
    1
   / \
  2   3
 /
4
```

## 7. Dry run

Entry order is [1, 2, 4, 3]. Node 2 gets interval [1, 3), covering itself and node 4 only.

## 8. Python implementation

Start with `ancestor_queries` in [implementation.py](implementation.py). Produce the result from the completed traversal.

## 9. Time and space complexity

For N nodes and Q queries, expected time is O(N + Q) and auxiliary space O(N), excluding output.

## 10. Why the algorithm works

DFS completes every descendant before leaving a node. Therefore all descendant entry positions form one contiguous interval.

## 11. When to use it

Answer a batch of ancestry queries in constant time each after preprocessing.

## 12. When not to use it

Preorder intervals need rebuilding after a structural edit.

## 13. Common mistakes

Use a half-open interval and define whether a node is its own ancestor.

## 14. Alternative approaches

For one query, follow mapped parents from the proposed descendant.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Record the preorder interval covered by each subtree. Use a half-open interval and define whether a node is its own ancestor.
