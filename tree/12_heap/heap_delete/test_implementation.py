from tree.heaps import BinaryHeap

from .implementation import heap_delete


def test_update_and_peak():
    heap = BinaryHeap([3, 5, 8])
    assert heap_delete(heap) == 3
    assert [heap.pop() for _ in range(len(heap))] == [5, 8]
