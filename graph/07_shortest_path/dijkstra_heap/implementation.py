"""Dijkstra Using a Priority Queue."""

from graph.shortest_paths import WeightedGraph, heap_distances


def dijkstra_heap(graph: WeightedGraph, source: int) -> list[float]:
    """Return shortest distances using a heap and nonnegative weights."""
    return heap_distances(graph, [source])[0]


if __name__ == "__main__":
    print(dijkstra_heap([[(1, 2), (2, 8)], [(2, 3)], []], 0))
