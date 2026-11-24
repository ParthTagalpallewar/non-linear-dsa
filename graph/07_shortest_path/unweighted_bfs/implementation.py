"""Unweighted Shortest Paths Using BFS."""

from collections import deque
from math import inf


def unweighted_bfs(graph: list[list[int]], source: int) -> list[float]:
    """Return shortest edge counts, with infinity for unreachable vertices."""
    if not 0 <= source < len(graph):
        raise IndexError("source outside the graph")
    distance = [inf] * len(graph)
    distance[source] = 0
    queue = deque([source])
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if distance[neighbor] == inf:
                distance[neighbor] = distance[vertex] + 1
                queue.append(neighbor)
    return distance
