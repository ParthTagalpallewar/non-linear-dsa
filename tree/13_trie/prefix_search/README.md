# Prefix Search

**P1**

## 1. What is the algorithm?

Check whether the trie has a path for the given prefix. The empty prefix always exists.

## 2. Problem it solves

Check whether the trie has a path for the given prefix. The empty prefix always exists.

## 3. Core intuition

Follow character edges and accept any final node without consulting its word marker.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Start at the empty prefix.
2. Follow character edges and accept any final node without consulting its word marker.
3. Return the result for the completed prefix or key.

## 6. Visual example

```text
(root)
  c ─ a ┬ t*
        └ r*
* = complete word
```

## 7. Dry run

Searching ca succeeds because both cat and car follow that path.

## 8. Python implementation

Start with `prefix_search` in [implementation.py](implementation.py). Return the result for the completed prefix or key.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For L characters, expected time O(L + 1) and O(1) auxiliary space.

## 10. Why the algorithm works

A nonempty existing prefix leads to a terminal somewhere below it because unused tails are pruned.

## 11. When to use it

Check whether the trie has a path for the given prefix. The empty prefix always exists.

## 12. When not to use it

A trie can use more memory than a flat collection if keys share few prefixes.

## 13. Common mistakes

Distinguish searching a prefix from searching a complete word.

## 14. Alternative approaches

A hash set is simpler when only exact membership queries matter.

## 15. Practice problems

- LeetCode #208, Medium. Prefix lookup with optional terminal marker. [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Follow character edges and accept any final node without consulting its word marker. Distinguish searching a prefix from searching a complete word.
