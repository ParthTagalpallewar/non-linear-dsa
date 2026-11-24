"""Fenwick Range Update."""

from tree.range_structures import RangeFenwick


def fenwick_range_update(tree: RangeFenwick, left: int, right: int, delta: int) -> None:
    """Add delta throughout a half-open interval using difference updates."""
    tree.range_add(left, right, delta)
