"""Connected Components Using BFS."""

from collections import deque


def components_bfs(graph: list[list[int]]) -> list[list[int]]:
    """Find components of a symmetric adjacency list with in-range IDs."""
    groups = []
    visited: set[int] = set()
    for seed in range(len(graph)):
        if seed in visited:
            continue
        visited.add(seed)
        pending = deque([seed])
        group = []
        while pending:
            vertex = pending.popleft()
            group.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    pending.append(neighbor)
        groups.append(group)
    return groups


if __name__ == "__main__":
    print(components_bfs([[1], [0], []]))
