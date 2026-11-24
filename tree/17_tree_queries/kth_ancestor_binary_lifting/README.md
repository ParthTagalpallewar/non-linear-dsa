# Kth Ancestor Using Binary Lifting

**P2**

## 1. What is the algorithm?

Find how far upward a specified number of parent steps lands.

## 2. Problem it solves

Find how far upward a specified number of parent steps lands.

## 3. Core intuition

Decompose k into set bits, then apply one already indexed ancestor jump per bit.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Root the undirected tree and preprocess the indicated index.
2. Decompose k into set bits, then apply one already indexed ancestor jump per bit.
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

On a depth-six chain, k=5 is binary 101. Jump by one and four edges to land at depth one.

## 8. Python implementation

Start with `kth_ancestor_binary_lifting` in [implementation.py](implementation.py). Return the result for each requested vertex or pair.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes, worst-case O(log(N + 1)) time per query, plus the shared table's O(N log(N + 1)) build time and space.

## 10. Why the algorithm works

Following a fixed number of parent links is independent of how the total is split across jumps.

## 11. When to use it

Find how far upward a specified number of parent steps lands.

## 12. When not to use it

The index assumes a fixed tree structure. Rebuild it after edges change.

## 13. Common mistakes

Reject k above the node's depth before indexing the jump table.

## 14. Alternative approaches

For very few queries, traverse the tree directly.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Decompose k into set bits, then apply one already indexed ancestor jump per bit. Reject k above the node's depth before indexing the jump table.
