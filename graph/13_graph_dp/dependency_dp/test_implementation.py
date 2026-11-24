import pytest

from .implementation import dependency_dp


def test_shared_dependency_is_charged_for_each_occurrence():
    assert dependency_dp([[], [0], [0], [1, 2]], [2, 3, 4, 1]) == [2, 5, 6, 12]


def test_rejects_cycle_and_length_mismatch():
    with pytest.raises(ValueError):
        dependency_dp([[0]], [1])
    with pytest.raises(ValueError):
        dependency_dp([], [1])
