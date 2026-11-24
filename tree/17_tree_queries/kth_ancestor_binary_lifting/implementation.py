"""Kth Ancestor Using Binary Lifting."""

from tree.queries import BinaryLifting


def kth_ancestor_binary_lifting(
    index: BinaryLifting, vertex: int, k: int
) -> int | None:
    """Return the vertex k parent links above vertex, if it exists."""
    return index.kth_ancestor(vertex, k)
