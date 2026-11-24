"""Adjacency List."""

from collections.abc import Iterable


def adjacency_list(
    vertex_count: int, edges: Iterable[tuple[int, int]], *, directed: bool = False
) -> list[list[int]]:
    """Build neighbor lists for vertices in range(vertex_count)."""
    if vertex_count < 0:
        raise ValueError("vertex count must be nonnegative")
    neighbors = [[] for _ in range(vertex_count)]
    for source, target in edges:
        if not (0 <= source < vertex_count and 0 <= target < vertex_count):
            raise ValueError("edge endpoint is outside the graph")
        neighbors[source].append(target)
        if not directed:
            neighbors[target].append(source)
    return neighbors
