# DAG Task Scheduling

**P1**

## 1. What is the algorithm?

DAG Task Scheduling answers a structural question about a graph.

## 2. Problem it solves

Calculate when tasks can finish given precedence constraints.

## 3. Core intuition

Process tasks in topological order and start each task at the latest finish among its immediate predecessors.

## 4. Prerequisites

Adjacency lists, vertex indexing, and the traversal used by the implementation.

## 5. How it works

1. Initialize per-vertex state.
2. Process tasks in topological order and start each task at the latest finish among its immediate predecessors.
3. Use the final state to produce the result.

## 6. Visual example

```text
0 (3) ─┐
       ├→ 2 (2)
1 (7) ─┘
```

## 7. Dry run

With 0 and 1 taking 3 and 7 days, 2 starts at day 7. Its 2-day duration gives a finish at day 9.

## 8. Python implementation

Start with `dag_task_scheduling` in [implementation.py](implementation.py). Use the final state to produce the result.

## 9. Time and space complexity

For V vertices and E edges, time is O(V + E) and auxiliary space is O(V). Each vertex is scheduled once and its adjacency is scanned once.

## 10. Why the algorithm works

All predecessor finish times are final by the time a task is processed. With unlimited workers that maximum is both a lower bound and a feasible start.

## 11. When to use it

Calculate when tasks can finish given precedence constraints.

## 12. When not to use it

Limited workers or shared resources can delay tasks beyond this schedule.

## 13. Common mistakes

Use a maximum across predecessors, and include the current task's own duration.

## 14. Alternative approaches

Compare the search state with the other implementations in this topic.

## 15. Practice problems

**Original exercise · P1.** Modify the example to include an isolated vertex and predict how the result changes.

## 16. Interview revision notes

Process tasks in topological order and start each task at the latest finish among its immediate predecessors. Use a maximum across predecessors, and include the current task's own duration.
