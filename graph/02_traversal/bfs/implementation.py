"""Breadth-First Search."""

from collections import deque


def bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """Return reachable vertices in discovery order. Missing keys are sinks."""
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


if __name__ == "__main__":
    print(bfs({0: [1, 2], 1: [3]}, 0))
