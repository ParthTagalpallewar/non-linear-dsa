"""Binary Indexed Tree Construction."""

from tree.range_structures import FenwickTree


def fenwick_construction(values: list[int]) -> FenwickTree:
    """Build a Fenwick index in linear time."""
    return FenwickTree(values)
