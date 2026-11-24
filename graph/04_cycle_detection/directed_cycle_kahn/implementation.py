"""Directed Cycle Detection Using Kahn’s Algorithm."""

from graph.topological import kahn_order


def directed_cycle_kahn(graph: list[list[int]]) -> bool:
    """A directed cycle exists if some vertices cannot be removed."""
    return len(kahn_order(graph)) != len(graph)
