"""Fenwick Prefix Sum Query."""

from tree.range_structures import FenwickTree


def fenwick_prefix_sum(tree: FenwickTree, end: int) -> int:
    """Perform a zero-based Fenwick prefix sum."""
    return tree.prefix_sum(end)
