"""Ford–Fulkerson."""

from graph.flow import CapacityEdge, path_flow, residual_network


def ford_fulkerson(size: int, edges: list[CapacityEdge], source: int, sink: int) -> int:
    """Compute maximum integral flow using depth-first augmenting paths."""
    graph = residual_network(size, edges, source, sink)
    return path_flow(graph, source, sink, breadth_first=False)
