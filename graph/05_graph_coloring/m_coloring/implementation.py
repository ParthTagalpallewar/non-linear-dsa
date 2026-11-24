"""M-Coloring Using Backtracking."""


def m_coloring(graph: list[list[int]], palette_size: int) -> list[int] | None:
    """Color a symmetric adjacency list using colors 0 through palette_size−1."""
    if palette_size < 0:
        raise ValueError("palette size must be nonnegative")
    if any(vertex in adjacent for vertex, adjacent in enumerate(graph)):
        return None
    colors = [-1] * len(graph)

    def assign(vertex: int) -> bool:
        if vertex == len(graph):
            return True
        forbidden = {colors[neighbor] for neighbor in graph[vertex]}
        for color in range(palette_size):
            if color not in forbidden:
                colors[vertex] = color
                if assign(vertex + 1):
                    return True
                colors[vertex] = -1
        return False

    return colors if assign(0) else None
