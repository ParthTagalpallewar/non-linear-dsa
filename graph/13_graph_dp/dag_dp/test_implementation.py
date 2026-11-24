import pytest

from .implementation import dag_dp


def test_best_path_can_begin_after_negative_prefix():
    assert dag_dp([[1, 2], [2], [], []], [-4, 5, 4, -3]) == [-4, 5, 9, -3]


def test_empty_and_cycle():
    assert dag_dp([], []) == []
    with pytest.raises(ValueError):
        dag_dp([[0]], [1])
