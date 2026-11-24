"""Fleury’s Algorithm."""

from graph.euler import Edge, euler_setup


def fleury(vertex_count: int, edges: list[Edge]) -> list[int] | None:
    """Build an undirected Euler walk by avoiding bridges when possible."""
    setup = euler_setup(vertex_count, edges)
    if setup is None:
        return None
    if not vertex_count:
        return []
    graph, vertex = setup
    active = [True] * len(edges)
    route = [vertex]

    for _ in edges:
        candidates = [(target, edge) for target, edge in graph[vertex] if active[edge]]
        if not candidates:
            return None
        for target, edge in candidates:
            active[edge] = False
            if len(candidates) == 1:
                break
            seen = {vertex}
            pending = [vertex]
            while pending and target not in seen:
                for neighbor, link in graph[pending.pop()]:
                    if active[link] and neighbor not in seen:
                        seen.add(neighbor)
                        pending.append(neighbor)
            if target in seen:
                break
            active[edge] = True
        else:
            target, edge = candidates[0]
            active[edge] = False
        vertex = target
        route.append(vertex)
    return route
