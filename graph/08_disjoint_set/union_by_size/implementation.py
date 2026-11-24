"""Union by Size."""

from graph.disjoint_set import DisjointSet


def union_by_size(sets: DisjointSet, first: int, second: int) -> bool:
    """Merge the two sets using the shared size-based implementation."""
    return sets.union(first, second)
