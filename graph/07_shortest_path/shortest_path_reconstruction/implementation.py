"""Shortest Path Reconstruction."""

from math import inf

from graph.shortest_paths import WeightedGraph, heap_distances


def shortest_path_reconstruction(
    graph: WeightedGraph, source: int, target: int
) -> list[int]:
    """Return one cheapest path, or an empty list when unreachable."""
    if not 0 <= target < len(graph):
        raise IndexError("target outside the graph")
    distance, parent = heap_distances(graph, [source])
    if distance[target] == inf:
        return []
    path = [target]
    while (previous := parent[path[-1]]) is not None:
        path.append(previous)
    return path[::-1]
