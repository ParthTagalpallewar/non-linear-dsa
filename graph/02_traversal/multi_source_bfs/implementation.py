"""Multi-Source BFS."""

from collections import deque
from collections.abc import Iterable


def multi_source_bfs(
    graph: dict[int, list[int]], sources: Iterable[int]
) -> dict[int, int]:
    """Map reachable vertices to their fewest edges from any source."""
    distance = dict.fromkeys(sources, 0)
    queue = deque(distance)
    while queue:
        vertex = queue.popleft()
        for neighbor in graph.get(vertex, []):
            if neighbor not in distance:
                distance[neighbor] = distance[vertex] + 1
                queue.append(neighbor)
    return distance
