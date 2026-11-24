"""Kahn’s Algorithm."""

from graph.topological import kahn_order


def kahn(graph: list[list[int]]) -> list[int]:
    """Return a topological order or raise ValueError if a cycle exists."""
    order = kahn_order(graph)
    if len(order) != len(graph):
        raise ValueError("graph has a directed cycle")
    return order


if __name__ == "__main__":
    print(kahn([[1, 2], [2], []]))
