"""Dynamic Programming on DAGs."""

from graph.topological import kahn_order


def dag_dp(graph: list[list[int]], values: list[int]) -> list[int]:
    """Find the best vertex-value path ending at each vertex, starting anywhere."""
    if len(graph) != len(values):
        raise ValueError("provide one value per vertex")
    order = kahn_order(graph)
    if len(order) != len(graph):
        raise ValueError("graph has a directed cycle")
    best = values.copy()
    for vertex in order:
        for target in graph[vertex]:
            best[target] = max(best[target], best[vertex] + values[target])
    return best
