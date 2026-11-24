import pytest

from .implementation import topological_sort_dfs


def test_dependencies_precede_consumers():
    assert topological_sort_dfs([[2], [2], [], []]) == [3, 1, 0, 2]
    assert topological_sort_dfs([]) == []


def test_cycle_raises():
    with pytest.raises(ValueError):
        topological_sort_dfs([[1], [0]])
