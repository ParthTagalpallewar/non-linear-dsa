# Union by Rank

**P1**

## 1. What is the algorithm?

Keep parent trees shallow using an upper bound on height.

## 2. Problem it solves

Keep parent trees shallow using an upper bound on height.

## 3. Core intuition

Attaching a shallower tree beneath a taller one preserves the taller rank.

## 4. Prerequisites

Parent arrays, forests, and connected components.

## 5. How it works

1. Find both roots.
2. Attach lower rank beneath higher rank.
3. Increase the winner's rank only on a tie.

## 6. Visual example

```text
0 ← 1 ← 2    3
```

## 7. Dry run

Merge 0 with 1 and 2 with 3 to get two rank-one roots. Merging those roots creates rank two.

## 8. Python implementation

Start with `RankDisjointSet` in [implementation.py](implementation.py). Increase the winner's rank only on a tie.

## 9. Time and space complexity

For V elements, storage and setup are O(V). With path halving, operations take O(α(V)) amortized.

## 10. Why the algorithm works

Rank changes only when equal heights could increase by one. A root of rank r represents at least 2^r elements.

## 11. When to use it

Keep parent trees shallow using an upper bound on height.

## 12. When not to use it

Standard DSU supports merges and queries. Deleting an edge can split a set and requires another approach.

## 13. Common mistakes

A repeated union cannot increase rank.

## 14. Alternative approaches

Compare with the other DSU variants in this topic.

## 15. Practice problems

**Original exercise · P1.** Trace the parent array across two merges and a redundant union.

## 16. Interview revision notes

Attaching a shallower tree beneath a taller one preserves the taller rank. A repeated union cannot increase rank.
