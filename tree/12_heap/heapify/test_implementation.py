import pytest

from .implementation import heapify


def test_larger_child_chosen_for_max_order():
    values = [1, 6, 7, 4, 5]
    heapify(values, 0, reverse=True)
    assert values == [7, 6, 1, 4, 5]
    with pytest.raises(IndexError):
        heapify([], 0)
