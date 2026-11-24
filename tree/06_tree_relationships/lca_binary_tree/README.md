# Lowest Common Ancestor in a Binary Tree

**P1**

## 1. What is the algorithm?

Find the deepest node above both query nodes, including a query node itself.

## 2. Problem it solves

Find the deepest node above both query nodes, including a query node itself.

## 3. Core intuition

Index parent links, then mark one ancestor chain and walk the second until the chains meet.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. Index parent links, then mark one ancestor chain and walk the second until the chains meet.
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

For nodes 4 and 3, mark 4→2→1. Walking 3→1 meets that chain at 1.

## 8. Python implementation

Start with `lca_binary_tree` in [implementation.py](implementation.py). Produce the result from the completed traversal.

Run the example from the repository root with `uv run python -m tree.06_tree_relationships.lca_binary_tree.implementation`.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes, worst-case time and auxiliary space are O(N) due to parent indexing.

## 10. Why the algorithm works

Ancestor chains converge exactly at their lowest common ancestor and share all nodes above it.

## 11. When to use it

Find the deepest node above both query nodes, including a query node itself.

## 12. When not to use it

Rebuilding the parent index per query is wasteful for many queries on one static tree.

## 13. Common mistakes

Compare node references rather than values and decide how to handle missing targets.

## 14. Alternative approaches

Binary lifting preprocesses a static tree for logarithmic LCA queries.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Index parent links, then mark one ancestor chain and walk the second until the chains meet. Compare node references rather than values and decide how to handle missing targets.
