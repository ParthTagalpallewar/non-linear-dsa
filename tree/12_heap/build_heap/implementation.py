"""Build Heap."""

from tree.heaps import BinaryHeap


def build_heap(values: list[int], *, reverse: bool = False) -> list[int]:
    """Return a heapified copy using bottom-up construction."""
    return BinaryHeap(values, reverse=reverse).data
