"""Minimum Source–Sink Cut."""

from graph.flow import CapacityEdge, path_flow, residual_network


def minimum_cut(
    size: int, edges: list[CapacityEdge], source: int, sink: int
) -> tuple[int, set[int], list[int]]:
    """Return cut capacity, source-side vertices, and crossing edge indices."""
    residual = residual_network(size, edges, source, sink)
    value = path_flow(residual, source, sink, breadth_first=True)
    seen = {source}
    pending = [source]
    for vertex in pending:
        for arc in residual[vertex]:
            if arc.capacity and arc.target not in seen:
                seen.add(arc.target)
                pending.append(arc.target)
    crossing = [
        i
        for i, (left, right, _) in enumerate(edges)
        if left in seen and right not in seen
    ]
    return value, seen, crossing
