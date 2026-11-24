"""Longest Path in a DAG."""

from math import inf

from graph.shortest_paths import WeightedGraph
from graph.topological import kahn_order


def longest_path_dag(graph: WeightedGraph, source: int) -> list[float]:
    """Return maximum path weights from source, or negative infinity."""
    if not 0 <= source < len(graph):
        raise IndexError("source outside the graph")
    order = kahn_order([[target for target, _ in edges] for edges in graph])
    if len(order) != len(graph):
        raise ValueError("graph has a directed cycle")
    best = [-inf] * len(graph)
    best[source] = 0
    for vertex in order:
        for target, weight in graph[vertex]:
            best[target] = max(best[target], best[vertex] + weight)
    return best
