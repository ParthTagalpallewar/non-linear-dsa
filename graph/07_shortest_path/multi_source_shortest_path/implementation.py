"""Multi-Source Weighted Shortest Paths."""

from graph.shortest_paths import WeightedGraph, heap_distances


def multi_source_shortest_path(graph: WeightedGraph, sources: list[int]) -> list[float]:
    """Return distances to each vertex from the closest supplied source."""
    return heap_distances(graph, sources)[0]
