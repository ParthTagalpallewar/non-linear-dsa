import pytest

from .implementation import prufer_encode


def test_smallest_leaf_drives_encoding():
    graph = [[1, 2], [0, 3, 4], [0], [1], [1]]
    assert prufer_encode(graph) == [0, 1, 1]
    assert prufer_encode([[1], [0]]) == []
    with pytest.raises(ValueError):
        prufer_encode([[]])
