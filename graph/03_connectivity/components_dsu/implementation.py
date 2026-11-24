"""Connected Components Using DSU."""

from graph.disjoint_set import DisjointSet


def components_dsu(graph: list[list[int]]) -> list[list[int]]:
    """Group vertices by representative. Neighbor IDs must be in range."""
    sets = DisjointSet(len(graph))
    for vertex, adjacent in enumerate(graph):
        for neighbor in adjacent:
            sets.union(vertex, neighbor)
    groups: dict[int, list[int]] = {}
    for vertex in range(len(graph)):
        groups.setdefault(sets.find(vertex), []).append(vertex)
    return list(groups.values())
