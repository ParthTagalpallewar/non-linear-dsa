"""Connected Components Using DFS."""


def components_dfs(graph: list[list[int]]) -> list[list[int]]:
    """Find components of a symmetric adjacency list with in-range IDs."""
    groups = []
    visited: set[int] = set()
    for seed in range(len(graph)):
        if seed in visited:
            continue
        visited.add(seed)
        pending = [seed]
        group = []
        while pending:
            vertex = pending.pop()
            group.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    pending.append(neighbor)
        groups.append(group)
    return groups
