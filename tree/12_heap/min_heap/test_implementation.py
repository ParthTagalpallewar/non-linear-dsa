import pytest

from .implementation import min_heap


def test_pop_order_and_empty():
    heap = min_heap([3, -1, 3, 8, 0])
    assert [heap.pop() for _ in range(len(heap))] == [-1, 0, 3, 3, 8]
    with pytest.raises(IndexError):
        heap.pop()
