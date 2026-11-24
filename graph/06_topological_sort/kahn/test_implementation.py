import pytest

from .implementation import kahn


def test_parallel_edges_and_isolates():
    assert kahn([[2, 2], [2], [], []]) == [0, 1, 3, 2]
    assert kahn([]) == []


def test_cycle_raises():
    with pytest.raises(ValueError):
        kahn([[0]])
