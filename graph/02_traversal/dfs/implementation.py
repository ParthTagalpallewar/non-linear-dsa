"""Recursive Depth-First Search."""


def dfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """Return recursive preorder. Missing keys are sinks."""
    visited: set[int] = set()
    order: list[int] = []

    def visit(vertex: int) -> None:
        visited.add(vertex)
        order.append(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return order
