"""Dynamic Connectivity with Insertions."""

from collections.abc import Iterable

from graph.disjoint_set import DisjointSet


def dynamic_connectivity(
    size: int, operations: Iterable[tuple[str, int, int]]
) -> list[bool]:
    """Answer connected queries interleaved with undirected edge additions."""
    sets = DisjointSet(size)
    answers = []
    for operation, first, second in operations:
        if operation == "add":
            sets.union(first, second)
        elif operation == "connected":
            answers.append(sets.find(first) == sets.find(second))
        else:
            raise ValueError(f"unknown operation: {operation}")
    return answers
