"""Segment Tree Point Update."""

from tree.range_structures import SegmentTree


def point_update(tree: SegmentTree, index: int, value: int) -> None:
    """Assign a new value at exactly one index."""
    tree.point_set(index, value)
