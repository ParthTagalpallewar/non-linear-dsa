# Serialization and Deserialization Using DFS

**P1**

## 1. What is the algorithm?

Encode and restore all binary-tree values and child positions.

## 2. Problem it solves

Encode and restore all binary-tree values and child positions.

## 3. Core intuition

Explicit null tokens remove shape ambiguity when reading a preorder stream of recursive subtrees.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. Explicit null tokens remove shape ambiguity when reading a preorder stream of recursive subtrees.
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

For the pictured tree the serialized sequence is "1,2,4,#,#,#,3,#,#". Each # occupies a child slot that has no accompanying subtree.

## 8. Python implementation

Start with `serialize_dfs` in [implementation.py](implementation.py). Produce the result from the completed traversal.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes and L encoded characters, run time is O(N + L) ignoring integer conversion costs for unusually large integers. Auxiliary space is O(N + L) for token storage and traversal state.

## 10. Why the algorithm works

Each non-null token creates exactly two expected child slots. The traversal order fully determines which slot is next, so the stream is uniquely invertible.

## 11. When to use it

Encode and restore all binary-tree values and child positions.

## 12. When not to use it

Very deep trees may exceed Python's recursion limit during decoding.

## 13. Common mistakes

Do not drop null tokens or let parsing silently ignore trailing data.

## 14. Alternative approaches

A BFS encoder pairs successive tokens with queued parents. A preorder encoder pairs recursive subtree encodings with their root.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Explicit null tokens remove shape ambiguity when reading a preorder stream of recursive subtrees. Do not drop null tokens or let parsing silently ignore trailing data.
