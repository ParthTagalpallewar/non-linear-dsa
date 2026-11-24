# Bitwise Trie

**P2**

## 1. What is the algorithm?

Index integers as root-to-leaf bit strings of equal length.

## 2. Problem it solves

Index integers as root-to-leaf bit strings of equal length.

## 3. Core intuition

Follow the most significant bit first so sharing early trie edges means sharing high bits.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Start at the empty prefix.
2. Follow the most significant bit first so sharing early trie edges means sharing high bits.
3. Return the result for the completed prefix or key.

## 6. Visual example

```text
(root)
  c ─ a ┬ t*
        └ r*
* = complete word
```

## 7. Dry run

At width 3, the values 1 and 3 are 001 and 011. They share the first zero edge.

## 8. Python implementation

Start with `bitwise_trie` in [implementation.py](implementation.py). Return the result for the completed prefix or key.

## 9. Time and space complexity

For N inserted values and width B, there are O(NB) operations and up to O(NB) stored nodes. Per-value updates need O(1) working space at fixed B.

## 10. Why the algorithm works

Every inserted integer follows one complete path of exactly B edges, and no two different fixed-width values use the same full path.

## 11. When to use it

Index integers as root-to-leaf bit strings of equal length.

## 12. When not to use it

A trie can use more memory than a flat collection if keys share few prefixes.

## 13. Common mistakes

Keep leading zeros and reject values wider than the width.

## 14. Alternative approaches

Direct bit comparison works when only a small set of values is queried.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Follow the most significant bit first so sharing early trie edges means sharing high bits. Keep leading zeros and reject values wider than the width.
