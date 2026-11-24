"""Dijkstra Using a Priority Queue."""

from graph.shortest_paths import WeightedGraph, heap_distances


def dijkstra_heap(graph: WeightedGraph, source: int) -> list[float]:
    """Return shortest distances using a heap and nonnegative weights."""
    return heap_distances(graph, [source])[0]
