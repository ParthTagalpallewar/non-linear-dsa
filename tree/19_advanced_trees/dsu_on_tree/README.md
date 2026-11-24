# DSU on Tree Using Small-to-Large Merging

**P3**

## 1. What is the algorithm?

Count distinct labels over all subtrees by reusing child sets.

## 2. Problem it solves

Count distinct labels over all subtrees by reusing child sets.

## 3. Core intuition

Prefer merging the smaller set into the larger so expensive element transfers rarely recur.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Seed every node with a singleton set.
2. Record each child's result before merging its set into its parent.
3. Swap sets when needed so only the smaller one is iterated.

## 6. Visual example

```text
    0
   / \
  1   2
 / \
3   4
```

## 7. Dry run

If node 1 has color 7 and its children have colors 7 and 9, merging gives {7,9}. Its answer is 2 before its set is reused by node 0.

## 8. Python implementation

Start with `dsu_on_tree` in [implementation.py](implementation.py). Swap sets when needed so only the smaller one is iterated.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N vertices, expected time O(N log(N + 1)) and auxiliary space O(N), under constant-time set operations.

## 10. Why the algorithm works

The union of child sets and the parent's singleton is exactly the subtree color set. If a merge causes little set growth, many duplicate entries are discarded permanently. Otherwise surviving transferred entries move into a substantially larger set.

## 11. When to use it

Count distinct labels over all subtrees by reusing child sets.

## 12. When not to use it

Use these routines on undirected trees with symmetric adjacency and integer IDs 0 through N−1.

## 13. Common mistakes

Save the child's answer before giving away its storage. Do not retain all intermediate sets.

## 14. Alternative approaches

For an offline array of Euler intervals, distinct-count queries can use a Fenwick sweep over last occurrences.

## 15. Practice problems

**Original exercise · P3.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Prefer merging the smaller set into the larger so expensive element transfers rarely recur. Save the child's answer before giving away its storage. Do not retain all intermediate sets.
