"""Static Path Sum Queries."""

from tree.queries import BinaryLifting
from tree.rooted import root_tree


def path_queries(
    graph: list[list[int]],
    values: list[int],
    pairs: list[tuple[int, int]],
    root: int = 0,
) -> list[int]:
    """Return inclusive node-value sums for static undirected tree paths."""
    if len(graph) != len(values):
        raise ValueError("provide one value per vertex")
    index = BinaryLifting(graph, root)
    tree = root_tree(graph, root)
    prefix = values.copy()
    for vertex in tree.order[1:]:
        prefix[vertex] += prefix[tree.parent[vertex]]
    result = []
    for left, right in pairs:
        ancestor = index.lca(left, right)
        result.append(
            prefix[left] + prefix[right] - 2 * prefix[ancestor] + values[ancestor]
        )
    return result
