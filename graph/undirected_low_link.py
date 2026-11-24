"""Shared DFS analysis for undirected multigraphs."""


def cuts(vertex_count: int, edges: list[tuple[int, int]]) -> tuple[list[int], set[int]]:
    """Return bridge edge indices and articulation vertices."""
    graph: list[list[tuple[int, int]]] = [[] for _ in range(vertex_count)]
    for edge, (left, right) in enumerate(edges):
        graph[left].append((right, edge))
        graph[right].append((left, edge))
    entry = [-1] * vertex_count
    low = [0] * vertex_count
    bridges: list[int] = []
    articulation: set[int] = set()
    clock = 0

    def visit(vertex: int, incoming: int) -> None:
        nonlocal clock
        entry[vertex] = low[vertex] = clock
        clock += 1
        children = 0
        for target, edge in graph[vertex]:
            if edge == incoming:
                continue
            if entry[target] != -1:
                low[vertex] = min(low[vertex], entry[target])
                continue
            children += 1
            visit(target, edge)
            low[vertex] = min(low[vertex], low[target])
            if low[target] > entry[vertex]:
                bridges.append(edge)
            if incoming != -1 and low[target] >= entry[vertex]:
                articulation.add(vertex)
        if incoming == -1 and children > 1:
            articulation.add(vertex)

    for vertex in range(vertex_count):
        if entry[vertex] == -1:
            visit(vertex, -1)
    return bridges, articulation
