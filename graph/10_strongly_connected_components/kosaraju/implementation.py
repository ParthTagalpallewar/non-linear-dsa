"""Kosaraju’s Algorithm."""


def kosaraju(graph: list[list[int]]) -> list[list[int]]:
    """Return strongly connected components of a directed adjacency list."""
    reverse: list[list[int]] = [[] for _ in graph]
    for vertex, adjacent in enumerate(graph):
        for target in adjacent:
            reverse[target].append(vertex)
    seen: set[int] = set()
    finish: list[int] = []

    def record(vertex: int) -> None:
        seen.add(vertex)
        for target in graph[vertex]:
            if target not in seen:
                record(target)
        finish.append(vertex)

    for vertex in range(len(graph)):
        if vertex not in seen:
            record(vertex)

    seen.clear()
    groups = []
    for vertex in reversed(finish):
        if vertex in seen:
            continue
        group = [vertex]
        seen.add(vertex)
        for current in group:
            for target in reverse[current]:
                if target not in seen:
                    seen.add(target)
                    group.append(target)
        groups.append(group)
    return groups
