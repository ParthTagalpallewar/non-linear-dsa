# Dynamic Programming on DAGs

**P2**

## 1. What is the algorithm?

Find the best score that can end at each state when transitions are acyclic.

## 2. Problem it solves

Find the best score that can end at each state when transitions are acyclic.

## 3. Core intuition

Store one optimal prefix score per state and extend it only after all its inputs are finalized.

## 4. Prerequisites

Graph representations and the traversal or recurrence used below.

## 5. How it works

1. Topologically order the graph.
2. Initialize every state with the score of starting there.
3. Propagate each finalized score to its successors.

## 6. Visual example

```text
0(−4) → 1(5) → 2(4)
```

## 7. Dry run

Values start at [−4, 5, 4]. Going from 0 to 1 gives 1, so 5 stays. Going from 1 to 2 gives 9.

## 8. Python implementation

Start with `dag_dp` in [implementation.py](implementation.py). Propagate each finalized score to its successors.

## 9. Time and space complexity

For V vertices and E edges, time is O(V + E), and auxiliary space is O(V) for ordering and state.

## 10. Why the algorithm works

Every path ending at v either starts there or ends with an edge u→v. The optimum over these possibilities is exact once u is final.

## 11. When to use it

Find the best score that can end at each state when transitions are acyclic.

## 12. When not to use it

Cyclic transitions need additional state or a different recurrence.

## 13. Common mistakes

Choose initialization according to whether paths may start anywhere or at one fixed source.

## 14. Alternative approaches

Memoized recursion over predecessor lists evaluates the same recurrence on demand.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example to introduce an isolated vertex, and predict the result before running the code.

## 16. Interview revision notes

Store one optimal prefix score per state and extend it only after all its inputs are finalized. Choose initialization according to whether paths may start anywhere or at one fixed source.
