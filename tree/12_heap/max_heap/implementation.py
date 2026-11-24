"""Max Heap."""

from collections.abc import Iterable

from tree.heaps import BinaryHeap


def max_heap(values: Iterable[int] = ()) -> BinaryHeap:
    """Construct a heap that exposes the largest element at the root."""
    return BinaryHeap(values, reverse=True)
