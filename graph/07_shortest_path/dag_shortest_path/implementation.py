"""Shortest Paths in a DAG."""

from math import inf

from graph.shortest_paths import WeightedGraph
from graph.topological import kahn_order


def dag_shortest_path(graph: WeightedGraph, source: int) -> list[float]:
    """Return single-source distances in a DAG, including negative weights."""
    if not 0 <= source < len(graph):
        raise IndexError("source outside the graph")
    order = kahn_order([[target for target, _ in edges] for edges in graph])
    if len(order) != len(graph):
        raise ValueError("graph has a directed cycle")
    distance = [inf] * len(graph)
    distance[source] = 0
    for vertex in order:
        for target, weight in graph[vertex]:
            distance[target] = min(distance[target], distance[vertex] + weight)
    return distance
