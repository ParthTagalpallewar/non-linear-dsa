from tree.heaps import BinaryHeap

from .implementation import heap_insert


def test_update_and_peak():
    heap = BinaryHeap([3, 5, 8])
    heap_insert(heap, 2)
    assert [heap.pop() for _ in range(len(heap))] == [2, 3, 5, 8]
