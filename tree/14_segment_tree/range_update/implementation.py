"""Range Update."""

from tree.range_structures import SegmentTree


def range_update(tree: SegmentTree, left: int, right: int, delta: int) -> None:
    """Add the same delta at every index in [left, right)."""
    tree.range_add(left, right, delta)
