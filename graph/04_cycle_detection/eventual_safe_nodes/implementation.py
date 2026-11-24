"""Eventual Safe Nodes."""

from graph.topological import kahn_order


def eventual_safe_nodes(graph: list[list[int]]) -> list[int]:
    """Return sorted vertices from which every walk eventually terminates."""
    reverse: list[list[int]] = [[] for _ in graph]
    for vertex, adjacent in enumerate(graph):
        for neighbor in adjacent:
            reverse[neighbor].append(vertex)
    safe = set(kahn_order(reverse))
    return [vertex for vertex in range(len(graph)) if vertex in safe]
