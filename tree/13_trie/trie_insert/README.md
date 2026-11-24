# Trie Insertion

**P1**

## 1. What is the algorithm?

Add a whole word while sharing existing prefix nodes.

## 2. Problem it solves

Add a whole word while sharing existing prefix nodes.

## 3. Core intuition

Reuse each existing character edge and create only missing edges.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Start at the empty prefix.
2. Reuse each existing character edge and create only missing edges.
3. Return the result for the completed prefix or key.

## 6. Visual example

```text
(root)
  c ─ a ┬ t*
        └ r*
* = complete word
```

## 7. Dry run

Adding car after cat reuses c→a and adds the r edge.

## 8. Python implementation

Start with `trie_insert` in [implementation.py](implementation.py). Return the result for the completed prefix or key.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For L characters, expected time O(L + 1), with up to O(L) newly stored nodes and O(1) working space.

## 10. Why the algorithm works

The final marked node spells the complete supplied word. Other routes remain intact.

## 11. When to use it

Add a whole word while sharing existing prefix nodes.

## 12. When not to use it

A trie can use more memory than a flat collection if keys share few prefixes.

## 13. Common mistakes

Mark the final prefix as a word even if every character edge already exists.

## 14. Alternative approaches

A hash set is simpler when only exact membership queries matter.

## 15. Practice problems

- LeetCode #208, Medium. Character edges and terminal markers. [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Reuse each existing character edge and create only missing edges. Mark the final prefix as a word even if every character edge already exists.
