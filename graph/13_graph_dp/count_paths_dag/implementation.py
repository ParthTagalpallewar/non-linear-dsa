"""Counting Paths in a DAG."""

from graph.topological import kahn_order


def count_paths_dag(graph: list[list[int]], source: int) -> list[int]:
    """Count edge-distinct paths from source, including its zero-edge path."""
    if not 0 <= source < len(graph):
        raise IndexError("source outside the graph")
    order = kahn_order(graph)
    if len(order) != len(graph):
        raise ValueError("graph has a directed cycle")
    paths = [0] * len(graph)
    paths[source] = 1
    for vertex in order:
        for target in graph[vertex]:
            paths[target] += paths[vertex]
    return paths
