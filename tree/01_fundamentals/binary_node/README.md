# Binary Tree Node

**P1**

## 1. What is the algorithm?

Build a reusable binary tree node with explicit child references.

## 2. Problem it solves

Build a reusable binary tree node with explicit child references.

## 3. Core intuition

Express each tree link through the parent node's child fields.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Create the desired child nodes first.
2. Supply the parent value and its children.
3. Leave children absent for a leaf.

## 6. Visual example

```text
    1
   / \
  2   3
 /
4
```

## 7. Dry run

Create leaf 4, then node 2 with 4 as its child. Supply 2 and 3 to the root constructor.

## 8. Python implementation

Start with `binary_node` in [implementation.py](implementation.py). Leave children absent for a leaf.

Run the example from the repository root with `uv run python -m tree.01_fundamentals.binary_node.implementation`.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

O(1) time and space per binary node.

## 10. Why the algorithm works

The child references connect previously built disjoint subtrees. If the caller supplies shared descendants or cycles, the result need not be a tree.

## 11. When to use it

Build a reusable binary tree node with explicit child references.

## 12. When not to use it

Use explicit adjacency lists when edges have arbitrary connectivity.

## 13. Common mistakes

Node values need not be unique. Identity-based queries require the actual node reference.

## 14. Alternative approaches

Arrays are convenient when complete binary trees can use arithmetic child indices.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Express each tree link through the parent node's child fields. Node values need not be unique. Identity-based queries require the actual node reference.
