"""Min Heap."""

from collections.abc import Iterable

from tree.heaps import BinaryHeap


def min_heap(values: Iterable[int] = ()) -> BinaryHeap:
    """Construct a heap that exposes the smallest element at the root."""
    return BinaryHeap(values, reverse=False)
