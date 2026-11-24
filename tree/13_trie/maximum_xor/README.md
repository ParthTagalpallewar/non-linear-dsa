# Maximum XOR Using a Bitwise Trie

**P2**

## 1. What is the algorithm?

Find the largest XOR among pairs of distinct list positions.

## 2. Problem it solves

Find the largest XOR among pairs of distinct list positions.

## 3. Core intuition

Choose an opposite bit whenever possible, from the most significant bit down.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Start at the empty prefix.
2. Choose an opposite bit whenever possible, from the most significant bit down.
3. Return the result for the completed prefix or key.

## 6. Visual example

```text
(root)
  c ─ a ┬ t*
        └ r*
* = complete word
```

## 7. Dry run

With 001 and 111 already indexed, query 010 prefers the path beginning with 1, giving XOR 101 against 111.

## 8. Python implementation

Start with `maximum_xor` in [implementation.py](implementation.py). Return the result for the completed prefix or key.

## 9. Time and space complexity

For N integers of maximum bit width B, there are O(NB) trie operations and O(NB) space. Python arbitrary-sized bit operations may have extra bit costs.

## 10. Why the algorithm works

Setting a higher XOR bit beats any possible combination of lower bits. Querying only earlier values covers every unordered pair once.

## 11. When to use it

Find the largest XOR among pairs of distinct list positions.

## 12. When not to use it

A trie can use more memory than a flat collection if keys share few prefixes.

## 13. Common mistakes

Query before insertion to enforce distinct input indices.

## 14. Alternative approaches

Exhaustive comparison uses O(N²) time and constant extra storage.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Choose an opposite bit whenever possible, from the most significant bit down. Query before insertion to enforce distinct input indices.
