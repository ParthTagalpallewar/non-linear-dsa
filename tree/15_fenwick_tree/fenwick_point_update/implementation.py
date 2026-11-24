"""Fenwick Point Update."""

from tree.range_structures import FenwickTree


def fenwick_point_update(tree: FenwickTree, index: int, delta: int) -> None:
    """Perform a zero-based Fenwick point update."""
    tree.add(index, delta)
