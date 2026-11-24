"""Adjacency Matrix."""

from collections.abc import Iterable


def adjacency_matrix(
    vertex_count: int, edges: Iterable[tuple[int, int]], *, directed: bool = False
) -> list[list[bool]]:
    """Build a Boolean matrix for vertices in range(vertex_count)."""
    if vertex_count < 0:
        raise ValueError("vertex count must be nonnegative")
    matrix = [[False] * vertex_count for _ in range(vertex_count)]
    for source, target in edges:
        if not (0 <= source < vertex_count and 0 <= target < vertex_count):
            raise ValueError("edge endpoint is outside the graph")
        matrix[source][target] = True
        if not directed:
            matrix[target][source] = True
    return matrix
