"""Shared adjacency and edge-walk construction for undirected multigraphs."""

Edge = tuple[int, int]
Adjacency = list[list[tuple[int, int]]]


def euler_setup(
    vertex_count: int, edges: list[Edge], *, closed: bool = False
) -> tuple[Adjacency, int] | None:
    """Build edge-indexed adjacency and choose a degree-compatible start."""
    if vertex_count < 0:
        raise ValueError("vertex count must be nonnegative")
    graph: Adjacency = [[] for _ in range(vertex_count)]
    for index, (left, right) in enumerate(edges):
        if not (0 <= left < vertex_count and 0 <= right < vertex_count):
            raise IndexError("edge endpoint outside the graph")
        graph[left].append((right, index))
        graph[right].append((left, index))
    odd = [vertex for vertex, adjacent in enumerate(graph) if len(adjacent) % 2]
    if odd and (closed or len(odd) != 2):
        return None
    start = odd[0] if odd else next((v for v, row in enumerate(graph) if row), 0)
    return graph, start


def edge_walk(
    vertex_count: int, edges: list[Edge], *, closed: bool = False
) -> list[int] | None:
    """Use Hierholzer's algorithm, or return None if no Euler walk exists."""
    setup = euler_setup(vertex_count, edges, closed=closed)
    if setup is None:
        return None
    if not vertex_count:
        return []
    graph, start = setup
    stack = [start]
    used = [False] * len(edges)
    reversed_walk = []
    while stack:
        vertex = stack[-1]
        if not graph[vertex]:
            reversed_walk.append(stack.pop())
            continue
        neighbor, edge = graph[vertex].pop()
        if not used[edge]:
            used[edge] = True
            stack.append(neighbor)
    if len(reversed_walk) != len(edges) + 1:
        return None
    return reversed_walk[::-1]
