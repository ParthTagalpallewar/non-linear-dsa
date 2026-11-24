"""Undirected Cycle Detection Using BFS."""

from collections import deque


def undirected_cycle_bfs(graph: list[list[int]]) -> bool:
    """Detect cycles in a symmetric adjacency list, including parallel edges."""
    visited: set[int] = set()
    for start in range(len(graph)):
        if start in visited:
            continue
        visited.add(start)
        pending = deque([(start, -1)])
        while pending:
            vertex, parent = pending.popleft()
            skipped_parent = False
            for neighbor in graph[vertex]:
                if neighbor == parent and not skipped_parent:
                    skipped_parent = True
                    continue
                if neighbor in visited:
                    return True
                visited.add(neighbor)
                pending.append((neighbor, vertex))
    return False
