# Convert Binary Tree to Doubly Linked List

**P1**

## 1. What is the algorithm?

Make an existing tree traversable forward and backward in inorder.

## 2. Problem it solves

Make an existing tree traversable forward and backward in inorder.

## 3. Core intuition

Track the last emitted node. Link the current node to that predecessor and link the predecessor forward.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. Track the last emitted node. Link the current node to that predecessor and link the predecessor forward.
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

For the example, the list is 4 ⇄ 2 ⇄ 1 ⇄ 3. The head is node 4 and the tail is node 3.

## 8. Python implementation

Start with `tree_to_doubly_linked_list` in [implementation.py](implementation.py). Produce the result from the completed traversal.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes and height H, worst-case time is O(N) and auxiliary space O(H + 1), excluding output.

## 10. Why the algorithm works

Inorder stack operations finish one left subtree before its parent. At each emission, the already completed prefix is linked and the original right subtree has been saved.

## 11. When to use it

Make an existing tree traversable forward and backward in inorder.

## 12. When not to use it

The operation destroys the original tree shape and creates bidirectional links.

## 13. Common mistakes

Set both pointer directions and preserve the current node's original right pointer before rewiring.

## 14. Alternative approaches

If the original tree needs to remain usable, allocate separate list nodes.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Track the last emitted node. Link the current node to that predecessor and link the predecessor forward. Set both pointer directions and preserve the current node's original right pointer before rewiring.
