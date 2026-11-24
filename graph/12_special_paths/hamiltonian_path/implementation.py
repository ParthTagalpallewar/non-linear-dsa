"""Hamiltonian Path Using Backtracking."""


def hamiltonian_path(graph: list[list[int]]) -> list[int] | None:
    """Visit every vertex exactly once in a directed path."""
    if not graph:
        return []
    used = [False] * len(graph)
    route: list[int] = []

    def extend(vertex: int, start: int) -> bool:
        if len(route) == len(graph):
            return True
        for target in graph[vertex]:
            if not used[target]:
                route.append(target)
                used[target] = True
                if extend(target, start):
                    return True
                used[target] = False
                route.pop()
        return False

    for start in range(len(graph)):
        used[start] = True
        route.append(start)
        if extend(start, start):
            return route
        route.pop()
        used[start] = False
    return None
