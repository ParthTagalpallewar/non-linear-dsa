"""DAG Task Scheduling."""

from graph.topological import kahn_order


def dag_task_scheduling(graph: list[list[int]], durations: list[int]) -> list[int]:
    """Return earliest finish times with unlimited workers and DAG constraints."""
    if len(graph) != len(durations) or any(duration < 0 for duration in durations):
        raise ValueError("provide one nonnegative duration per task")
    order = kahn_order(graph)
    if len(order) != len(graph):
        raise ValueError("dependencies contain a cycle")
    earliest_start = [0] * len(graph)
    finish = [0] * len(graph)
    for task in order:
        finish[task] = earliest_start[task] + durations[task]
        for next_task in graph[task]:
            earliest_start[next_task] = max(earliest_start[next_task], finish[task])
    return finish
