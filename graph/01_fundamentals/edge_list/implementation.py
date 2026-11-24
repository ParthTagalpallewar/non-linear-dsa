"""Edge List."""

from collections.abc import Iterable


def edge_list(
    vertex_count: int, edges: Iterable[tuple[int, int, int]]
) -> list[tuple[int, int, int]]:
    """Materialize ordered (source, target, weight) records without deduplication."""
    if vertex_count < 0:
        raise ValueError("vertex count must be nonnegative")
    result = []
    for source, target, weight in edges:
        if not (0 <= source < vertex_count and 0 <= target < vertex_count):
            raise ValueError("edge endpoint is outside the graph")
        result.append((source, target, weight))
    return result
