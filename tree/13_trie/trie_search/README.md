# Trie Search

**P1**

## 1. What is the algorithm?

Check whether a whole word is stored.

## 2. Problem it solves

Check whether a whole word is stored.

## 3. Core intuition

Follow every character and check that the final prefix is marked terminal.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Start at the empty prefix.
2. Follow every character and check that the final prefix is marked terminal.
3. Return the result for the completed prefix or key.

## 6. Visual example

```text
(root)
  c ─ a ┬ t*
        └ r*
* = complete word
```

## 7. Dry run

Searching ca reaches an internal node but fails unless ca is individually stored.

## 8. Python implementation

Start with `trie_search` in [implementation.py](implementation.py). Return the result for the completed prefix or key.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For L characters, O(L + 1) expected time and O(1) auxiliary space.

## 10. Why the algorithm works

A terminal path spells one exact stored word. Missing edges reject absent prefixes early.

## 11. When to use it

Check whether a whole word is stored.

## 12. When not to use it

A trie can use more memory than a flat collection if keys share few prefixes.

## 13. Common mistakes

A word can terminate at an internal node or the root.

## 14. Alternative approaches

A hash set is simpler when only exact membership queries matter.

## 15. Practice problems

- LeetCode #208, Medium. Exact lookup using a terminal marker. [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Follow every character and check that the final prefix is marked terminal. A word can terminate at an internal node or the root.
