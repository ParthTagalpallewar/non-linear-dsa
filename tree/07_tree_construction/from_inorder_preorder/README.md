# Construct from Inorder and Preorder

**P1**

## 1. What is the algorithm?

Recreate a uniquely defined tree from inorder and preorder.

## 2. Problem it solves

Recreate a uniquely defined tree from inorder and preorder.

## 3. Core intuition

Read the next root from the start of preorder. Its inorder position splits the remaining keys into two subtrees.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. Read the next root from the start of preorder. Its inorder position splits the remaining keys into two subtrees.
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

Inorder [4, 2, 1, 3] splits at root 1 into [4, 2] and [3]. Build the left subtree first to match the cursor's order.

## 8. Python implementation

Start with `from_inorder_preorder` in [implementation.py](implementation.py). Produce the result from the completed traversal.

## 9. Time and space complexity

For N nodes and height H, expected time is O(N) and auxiliary space O(N + H) for the index and stack.

## 10. Why the algorithm works

Each recursive call consumes the root of exactly its inorder slice. Distinct keys make the split unique and induction reconstructs both children.

## 11. When to use it

Recreate a uniquely defined tree from inorder and preorder.

## 12. When not to use it

Recursive implementations can reach Python's recursion limit on skewed trees.

## 13. Common mistakes

Advance the traversal cursor in the correct direction and recurse into the left side first.

## 14. Alternative approaches

Repeated linear search avoids a dictionary but can take O(N²) on skewed inputs.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Read the next root from the start of preorder. Its inorder position splits the remaining keys into two subtrees. Advance the traversal cursor in the correct direction and recurse into the left side first.
