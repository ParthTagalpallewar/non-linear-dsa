"""Range Sum Query."""

from tree.range_structures import SegmentTree


def range_sum_query(tree: SegmentTree, left: int, right: int) -> int:
    """Return the sum of the half-open interval."""
    if tree.aggregate != "sum":
        raise ValueError("expected a sum segment tree")
    return tree.query(left, right)
