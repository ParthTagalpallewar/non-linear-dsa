# Minimum Source–Sink Cut

**P2**

## 1. What is the algorithm?

Separate the source from the sink by removing directed capacity of minimum total weight.

## 2. Problem it solves

Separate the source from the sink by removing directed capacity of minimum total weight.

## 3. Core intuition

After maximum flow, residual reachability partitions the vertices along a saturated cut.

## 4. Prerequisites

Graph representations and the traversal or recurrence used below.

## 5. How it works

1. Run maximum flow on the residual graph.
2. Find all vertices still reachable from the source.
3. Collect original edges crossing from the reachable side to its complement.

## 6. Visual example

```text
s ─3→ a ─2→ t
 \2→ b ─4─↗
```

## 7. Dry run

After sending 4 units, s can reach a with the remaining unit on s→a. The cut crosses a→t and s→b, totaling 4.

## 8. Python implementation

Start with `minimum_cut` in [implementation.py](implementation.py). Collect original edges crossing from the reachable side to its complement.

## 9. Time and space complexity

For V vertices and E edges, maximum flow dominates at O(V E²) plus O(V + E) setup and extraction. Working space is O(V + E).

## 10. Why the algorithm works

Every original outgoing cut edge is saturated and incoming cut edges carry zero net opposing flow, since otherwise a positive residual arc could cross outward. The crossing capacity therefore equals the maximum flow.

## 11. When to use it

Separate the source from the sink by removing directed capacity of minimum total weight.

## 12. When not to use it

This computes a cut for fixed terminals, not a global minimum cut over all choices of terminals.

## 13. Common mistakes

Use residual reachability after the last augmentation, and report only original edges crossing outward.

## 14. Alternative approaches

Any valid maximum-flow engine can supply the residual capacities for cut extraction.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example to introduce an isolated vertex, and predict the result before running the code.

## 16. Interview revision notes

After maximum flow, residual reachability partitions the vertices along a saturated cut. Use residual reachability after the last augmentation, and report only original edges crossing outward.
