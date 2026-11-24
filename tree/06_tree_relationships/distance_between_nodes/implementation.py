"""Distance Between Two Nodes."""

from tree.nodes import BinaryNode
from tree.relationships import parent_index


def distance_between_nodes(
    root: BinaryNode | None, first: BinaryNode, second: BinaryNode
) -> int | None:
    """Return edge distance between present nodes, otherwise None."""
    parents = parent_index(root)
    if first not in parents or second not in parents:
        return None
    distances = {}
    current: BinaryNode | None = first
    depth = 0
    while current is not None:
        distances[current] = depth
        current = parents[current]
        depth += 1
    current = second
    depth = 0
    while current not in distances:
        current = parents[current]
        depth += 1
    return depth + distances[current]
