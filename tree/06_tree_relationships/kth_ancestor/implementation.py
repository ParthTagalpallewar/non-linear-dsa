"""Kth Ancestor of a Node."""

from tree.nodes import BinaryNode
from tree.relationships import parent_index


def kth_ancestor(
    root: BinaryNode | None, target: BinaryNode, k: int
) -> BinaryNode | None:
    """Climb k parent links. Return None if the node or ancestor is absent."""
    if k < 0:
        raise ValueError("k must be nonnegative")
    parents = parent_index(root)
    current = target if target in parents else None
    for _ in range(k):
        if current is None:
            break
        current = parents[current]
    return current
