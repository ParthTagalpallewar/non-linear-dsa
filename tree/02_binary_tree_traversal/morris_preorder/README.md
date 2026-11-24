# Morris Preorder Traversal

**P2**

## 1. What is the algorithm?

Traverse a mutable binary tree without recursion or an explicit stack.

## 2. Problem it solves

Traverse a mutable binary tree without recursion or an explicit stack.

## 3. Core intuition

The rightmost node of a left subtree has a spare right pointer that can record the return address.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. When a left subtree exists, find its rightmost node.
2. Create a temporary thread when first descending, and remove it when returning.
3. Emit before descending left.

## 6. Visual example

```text
    1
   / \
  2   3
 /
4
```

## 7. Dry run

Create the thread 2→1, then 4→2. After visiting 4, follow its thread to 2 and erase it. Repeat at 1.

## 8. Python implementation

Start with `morris_preorder` in [implementation.py](implementation.py). Emit before descending left.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes, time is O(N), with O(1) auxiliary space besides O(N) output. Each traversed edge is examined a constant number of times.

## 10. Why the algorithm works

A thread replaces precisely one pending return to a parent. Encountering it a second time proves the parent's left subtree has been exhausted.

## 11. When to use it

Traverse a mutable binary tree without recursion or an explicit stack.

## 12. When not to use it

Avoid Morris on immutable trees or when readers can see temporary changes during traversal.

## 13. Common mistakes

Compare node identities and restore each thread before advancing to the right.

## 14. Alternative approaches

Recursive or stack-based traversal leaves the tree unchanged throughout.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

The rightmost node of a left subtree has a spare right pointer that can record the return address. Compare node identities and restore each thread before advancing to the right.
