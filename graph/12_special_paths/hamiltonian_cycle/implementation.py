"""Hamiltonian Cycle Using Backtracking."""


def hamiltonian_cycle(graph: list[list[int]]) -> list[int] | None:
    """Visit every vertex exactly once and return to the start."""
    if not graph:
        return None
    used = [False] * len(graph)
    route: list[int] = []

    def extend(vertex: int, start: int) -> bool:
        if len(route) == len(graph):
            return start in graph[vertex]
        for target in graph[vertex]:
            if not used[target]:
                route.append(target)
                used[target] = True
                if extend(target, start):
                    return True
                used[target] = False
                route.pop()
        return False

    for start in range(1):
        used[start] = True
        route.append(start)
        if extend(start, start):
            return route + [start]
        route.pop()
        used[start] = False
    return None
