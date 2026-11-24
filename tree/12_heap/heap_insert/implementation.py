"""Heap Insertion."""

from tree.heaps import BinaryHeap


def heap_insert(heap: BinaryHeap, value: int) -> None:
    """Insert a value and repair its ancestor chain."""
    heap.push(value)
