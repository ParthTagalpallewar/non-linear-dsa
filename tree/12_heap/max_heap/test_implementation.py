import pytest

from .implementation import max_heap


def test_pop_order_and_empty():
    heap = max_heap([3, -1, 3, 8, 0])
    assert [heap.pop() for _ in range(len(heap))] == [8, 3, 3, 0, -1]
    with pytest.raises(IndexError):
        heap.pop()
