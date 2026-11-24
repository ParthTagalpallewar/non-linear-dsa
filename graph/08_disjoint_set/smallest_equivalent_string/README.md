# Lexicographically Smallest Equivalent String

**P1**

## 1. What is the algorithm?

Minimize a string when any character may be replaced by an equivalent one.

## 2. Problem it solves

Minimize a string when any character may be replaced by an equivalent one.

## 3. Core intuition

Equivalence is transitive, and the earliest differing character determines lexical order.

## 4. Prerequisites

Parent arrays, forests, and connected components.

## 5. How it works

1. Merge paired characters.
2. Scan characters in sorted order to record each class's minimum.
3. Replace each character with that minimum.

## 6. Visual example

```text
0 ← 1 ← 2    3
```

## 7. Dry run

With b equivalent to c and c equivalent to a, all three become a. The final z in cbaz remains z.

## 8. Python implementation

Start with `smallest_equivalent_string` in [implementation.py](implementation.py). Replace each character with that minimum.

## 9. Time and space complexity

For P pairs, T output characters and A distinct characters, expected time is O(A log A + (P + T + A) α(A)). Auxiliary space is O(P + T + A), including temporary input concatenation.

## 10. Why the algorithm works

DSU computes the equivalence closure. Choosing the smallest possible character at every independent position minimizes the whole string.

## 11. When to use it

Minimize a string when any character may be replaced by an equivalent one.

## 12. When not to use it

This model assumes position-independent single-character replacements.

## 13. Common mistakes

A DSU root chosen by size is not necessarily the smallest character.

## 14. Alternative approaches

Compare with the other DSU variants in this topic.

## 15. Practice problems

**Original exercise · P1.** Support an alternative ordering of equivalence-class members.

## 16. Interview revision notes

Equivalence is transitive, and the earliest differing character determines lexical order. A DSU root chosen by size is not necessarily the smallest character.
