import pytest

from .implementation import count_paths_dag


def test_diamond_parallel_edges_and_isolate():
    assert count_paths_dag([[1, 1, 2], [3], [3], [], []], 0) == [1, 2, 1, 3, 0]


def test_rejects_cycle():
    with pytest.raises(ValueError):
        count_paths_dag([[0]], 0)
