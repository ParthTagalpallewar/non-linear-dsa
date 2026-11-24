"""Range Min Query."""

from tree.range_structures import SegmentTree


def range_min_query(tree: SegmentTree, left: int, right: int) -> int:
    """Return the min of the half-open interval."""
    if tree.aggregate != "min":
        raise ValueError("expected a min segment tree")
    return tree.query(left, right)
