"""Range Max Query."""

from tree.range_structures import SegmentTree


def range_max_query(tree: SegmentTree, left: int, right: int) -> int:
    """Return the max of the half-open interval."""
    if tree.aggregate != "max":
        raise ValueError("expected a max segment tree")
    return tree.query(left, right)
