# Trie Deletion

**P1**

## 1. What is the algorithm?

Remove a stored word while retaining all shared prefixes.

## 2. Problem it solves

Remove a stored word while retaining all shared prefixes.

## 3. Core intuition

Clear the terminal bit and walk backward pruning childless nonterminals.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Start at the empty prefix.
2. Clear the terminal bit and walk backward pruning childless nonterminals.
3. Return the result for the completed prefix or key.

## 6. Visual example

```text
(root)
  c ─ a ┬ t*
        └ r*
* = complete word
```

## 7. Dry run

Deleting cat removes t but keeps c→a because car still uses it.

## 8. Python implementation

Start with `trie_delete` in [implementation.py](implementation.py). Return the result for the completed prefix or key.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For L characters, O(L + 1) expected time and O(L) auxiliary space for the backward path.

## 10. Why the algorithm works

A nonterminal with no children cannot lie on a route to any other complete word.

## 11. When to use it

Remove a stored word while retaining all shared prefixes.

## 12. When not to use it

A trie can use more memory than a flat collection if keys share few prefixes.

## 13. Common mistakes

Do not prune a shorter word or a prefix with another active branch.

## 14. Alternative approaches

A hash set is simpler when only exact membership queries matter.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Clear the terminal bit and walk backward pruning childless nonterminals. Do not prune a shorter word or a prefix with another active branch.
