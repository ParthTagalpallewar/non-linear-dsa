"""Heap Deletion."""

from tree.heaps import BinaryHeap


def heap_delete(heap: BinaryHeap) -> int:
    """Remove and return the extreme heap value."""
    return heap.pop()
