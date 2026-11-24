"""Subtree Queries Using an Euler Tour."""

from itertools import accumulate

from tree.rooted import root_tree


def subtree_queries(
    graph: list[list[int]], values: list[int], vertices: list[int], root: int = 0
) -> list[int]:
    """Return the sum within each requested subtree using preorder intervals."""
    if len(graph) != len(values):
        raise ValueError("provide one value per vertex")
    tree = root_tree(graph, root)
    prefix = [0, *accumulate(values[v] for v in tree.order)]
    result = []
    for vertex in vertices:
        if not 0 <= vertex < len(graph):
            raise IndexError("vertex outside the tree")
        result.append(prefix[tree.end[vertex]] - prefix[tree.start[vertex]])
    return result
