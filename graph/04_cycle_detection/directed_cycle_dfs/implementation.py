"""Directed Cycle Detection Using DFS."""


def directed_cycle_dfs(graph: list[list[int]]) -> bool:
    """Return whether DFS finds an edge to an active ancestor."""
    state = [0] * len(graph)

    def visit(vertex: int) -> bool:
        state[vertex] = 1
        for neighbor in graph[vertex]:
            if state[neighbor] == 1:
                return True
            if state[neighbor] == 0 and visit(neighbor):
                return True
        state[vertex] = 2
        return False

    return any(state[vertex] == 0 and visit(vertex) for vertex in range(len(graph)))
