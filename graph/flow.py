"""Residual-network primitives shared by the flow lessons."""

from collections import deque
from dataclasses import dataclass

CapacityEdge = tuple[int, int, int]


@dataclass
class Arc:
    """A residual arc and the location of its reverse arc."""

    target: int
    reverse: int
    capacity: int


def residual_network(
    size: int, edges: list[CapacityEdge], source: int, sink: int
) -> list[list[Arc]]:
    """Build paired arcs, validating the terminals and nonnegative capacities."""
    if not (0 <= source < size and 0 <= sink < size) or source == sink:
        raise ValueError("source and sink must be distinct in-range vertices")
    graph: list[list[Arc]] = [[] for _ in range(size)]
    for left, right, capacity in edges:
        if not (0 <= left < size and 0 <= right < size) or capacity < 0:
            raise ValueError("invalid capacity edge")
        if left == right:
            continue
        forward = Arc(right, len(graph[right]), capacity)
        back = Arc(left, len(graph[left]), 0)
        graph[left].append(forward)
        graph[right].append(back)
    return graph


def augment(graph: list[list[Arc]], vertex: int, arc: Arc, amount: int) -> None:
    """Send flow through one residual arc and allow cancelling it in reverse."""
    arc.capacity -= amount
    graph[arc.target][arc.reverse].capacity += amount


def path_flow(
    graph: list[list[Arc]], source: int, sink: int, *, breadth_first: bool
) -> int:
    """Repeatedly augment along DFS or BFS paths, mutating the residual graph."""
    result = 0
    while True:
        previous: dict[int, tuple[int, Arc]] = {}
        seen = {source}
        pending = deque([source])
        while pending and sink not in seen:
            vertex = pending.popleft() if breadth_first else pending.pop()
            for arc in graph[vertex]:
                if arc.capacity and arc.target not in seen:
                    seen.add(arc.target)
                    previous[arc.target] = vertex, arc
                    pending.append(arc.target)
        if sink not in seen:
            return result
        path = []
        vertex = sink
        while vertex != source:
            vertex, arc = previous[vertex]
            path.append((vertex, arc))
        amount = min(arc.capacity for _, arc in path)
        for vertex, arc in path:
            augment(graph, vertex, arc, amount)
        result += amount
