"""Edmonds–Karp."""

from graph.flow import CapacityEdge, path_flow, residual_network


def edmonds_karp(size: int, edges: list[CapacityEdge], source: int, sink: int) -> int:
    """Compute maximum integral flow using breadth-first augmenting paths."""
    graph = residual_network(size, edges, source, sink)
    return path_flow(graph, source, sink, breadth_first=True)
