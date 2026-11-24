"""Segment Tree Construction."""

from tree.range_structures import Aggregate, SegmentTree


def segment_tree_construction(
    values: list[int], aggregate: Aggregate = "sum"
) -> SegmentTree:
    """Build a zero-based segment tree for sum, minimum, or maximum."""
    return SegmentTree(values, aggregate)
