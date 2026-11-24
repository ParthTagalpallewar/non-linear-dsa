"""Shared indegree elimination for directed graphs."""

from collections import deque


def kahn_order(graph: list[list[int]]) -> list[int]:
    """Return the vertices removable by indegree elimination."""
    indegree = [0] * len(graph)
    for adjacent in graph:
        for neighbor in adjacent:
            indegree[neighbor] += 1
    queue = deque(v for v, degree in enumerate(indegree) if degree == 0)
    order = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return order
