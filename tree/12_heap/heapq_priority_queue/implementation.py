"""Priority Queue Using heapq."""

import heapq


def heapq_priority_queue(tasks: list[tuple[int, str]]) -> list[str]:
    """Run tasks by ascending priority, preserving arrival order on ties."""
    entries = [(priority, index, task) for index, (priority, task) in enumerate(tasks)]
    heapq.heapify(entries)
    return [heapq.heappop(entries)[2] for _ in tasks]
