"""0–1 BFS."""

from collections import deque
from math import inf

from graph.shortest_paths import WeightedGraph


def zero_one_bfs(graph: WeightedGraph, source: int) -> list[float]:
    """Return shortest distances when every edge has weight zero or one."""
    if not 0 <= source < len(graph):
        raise IndexError("source outside the graph")
    if any(w not in (0, 1) for adjacent in graph for _, w in adjacent):
        raise ValueError("edge weights must be zero or one")
    distance = [inf] * len(graph)
    distance[source] = 0
    pending = deque([(0, source)])
    while pending:
        current, vertex = pending.popleft()
        if current != distance[vertex]:
            continue
        for target, weight in graph[vertex]:
            candidate = current + weight
            if candidate < distance[target]:
                distance[target] = candidate
                if weight == 0:
                    pending.appendleft((candidate, target))
                else:
                    pending.append((candidate, target))
    return distance
