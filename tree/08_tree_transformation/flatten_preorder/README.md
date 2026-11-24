# Flatten Binary Tree into a Linked List

**P1**

## 1. What is the algorithm?

Reuse binary-tree nodes as a singly linked preorder chain.

## 2. Problem it solves

Reuse binary-tree nodes as a singly linked preorder chain.

## 3. Core intuition

Save original child pointers on a stack before rewriting links.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. Save original child pointers on a stack before rewriting links.
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

Preorder emits 1→2→4→3. Each emitted node loses its left pointer and links right to the next emitted node.

## 8. Python implementation

Start with `flatten_preorder` in [implementation.py](implementation.py). Produce the result from the completed traversal.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes and height H, worst-case time is O(N) and auxiliary space O(H + 1), excluding output.

## 10. Why the algorithm works

The stack generates ordinary preorder. Every consecutive pair in that traversal is connected once, and the final preorder node is a leaf.

## 11. When to use it

Reuse binary-tree nodes as a singly linked preorder chain.

## 12. When not to use it

The original shape cannot be recovered without additional data.

## 13. Common mistakes

Save children before changing pointers, and clear left links on every node.

## 14. Alternative approaches

Reverse preorder recursion can wire each node to a previously processed successor.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Save original child pointers on a stack before rewriting links. Save children before changing pointers, and clear left links on every node.
