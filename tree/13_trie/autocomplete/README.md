# Autocomplete Using a Trie

**P2**

## 1. What is the algorithm?

Return suggestions matching a partially typed prefix.

## 2. Problem it solves

Return suggestions matching a partially typed prefix.

## 3. Core intuition

Locate the prefix node once, then visit its terminal descendants in lexical order.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Start at the empty prefix.
2. Locate the prefix node once, then visit its terminal descendants in lexical order.
3. Return the result for the completed prefix or key.

## 6. Visual example

```text
(root)
  c ─ a ┬ t*
        └ r*
* = complete word
```

## 7. Dry run

From ca, emit ca itself if marked. Visit b, r, and t children in that order.

## 8. Python implementation

Start with `autocomplete` in [implementation.py](implementation.py). Return the result for the completed prefix or key.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For P prefix characters, U trie nodes scanned, D maximum branching, and output length S, expected time O(P + U log(D + 1) + S). Auxiliary space includes recursion depth and sorted child lists on its active path.

## 10. Why the algorithm works

Lexical order places a complete prefix before its longer extensions and places each character subtree before any subtree with a larger leading character.

## 11. When to use it

Return suggestions matching a partially typed prefix.

## 12. When not to use it

A trie can use more memory than a flat collection if keys share few prefixes.

## 13. Common mistakes

Return early for an absent prefix or a limit of zero.

## 14. Alternative approaches

A sorted array enables range lookup by binary search, with more expensive insertions.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Locate the prefix node once, then visit its terminal descendants in lexical order. Return early for an absent prefix or a limit of zero.
