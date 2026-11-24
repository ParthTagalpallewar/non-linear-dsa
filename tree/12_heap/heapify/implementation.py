"""Heapify."""

from tree.heaps import sift_down


def heapify(values: list[int], index: int, *, reverse: bool = False) -> None:
    """Repair the subtree at index in place, assuming valid child heaps."""
    if not 0 <= index < len(values):
        raise IndexError("index outside heap")
    sift_down(values, index, len(values), reverse)
