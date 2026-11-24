"""Fenwick Range Sum Query."""

from tree.range_structures import FenwickTree


def fenwick_range_sum(tree: FenwickTree, left: int, right: int) -> int:
    """Perform a zero-based Fenwick range sum."""
    return tree.range_sum(left, right)
