# Dependency-Based Dynamic Programming

**P2**

## 1. What is the algorithm?

Evaluate a cost recurrence in which each required item contributes its full cost.

## 2. Problem it solves

Evaluate a cost recurrence in which each required item contributes its full cost.

## 3. Core intuition

Resolve dependencies before their dependents so a computed total can be propagated without recomputing it.

## 4. Prerequisites

Graph representations and the traversal or recurrence used below.

## 5. How it works

1. Reverse prerequisite lists into dependent lists.
2. Topologically order tasks.
3. Add every finalized total to each dependent once per requirement.

## 6. Visual example

```text
base → left → final
  \──→ right ─↗
```

## 7. Dry run

Base costs 2, left 3, right 4, final 1 produce totals 2, 5, 6, and 12, counting base twice inside final.

## 8. Python implementation

Start with `dependency_dp` in [implementation.py](implementation.py). Add every finalized total to each dependent once per requirement.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V tasks and E requirements, there are O(V + E) arithmetic and graph operations and O(V + E) auxiliary space.

## 10. Why the algorithm works

By induction in topological order, every task has received exactly the totals of its listed prerequisites when its own total is propagated.

## 11. When to use it

Evaluate a cost recurrence in which each required item contributes its full cost.

## 12. When not to use it

If a shared prerequisite is paid once globally, this additive recurrence overcharges it.

## 13. Common mistakes

Distinguish an additive material cost from a parallel completion time, which takes the maximum prerequisite finish.

## 14. Alternative approaches

Use a set union recurrence when the result needs the identity of every unique prerequisite.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example to introduce an isolated vertex, and predict the result before running the code.

## 16. Interview revision notes

Resolve dependencies before their dependents so a computed total can be propagated without recomputing it. Distinguish an additive material cost from a parallel completion time, which takes the maximum prerequisite finish.
