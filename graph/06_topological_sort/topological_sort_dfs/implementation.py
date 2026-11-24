"""Topological Sort Using DFS."""


def topological_sort_dfs(graph: list[list[int]]) -> list[int]:
    """Return reverse finishing order or raise ValueError on a cycle."""
    state = [0] * len(graph)
    order: list[int] = []

    def visit(vertex: int) -> None:
        if state[vertex] == 1:
            raise ValueError("graph has a directed cycle")
        if state[vertex] == 2:
            return
        state[vertex] = 1
        for neighbor in graph[vertex]:
            visit(neighbor)
        state[vertex] = 2
        order.append(vertex)

    for vertex in range(len(graph)):
        visit(vertex)
    return order[::-1]
