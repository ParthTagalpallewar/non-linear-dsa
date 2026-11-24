from math import inf

import pytest

from .implementation import longest_path_dag


def test_negative_path_and_unreachable_vertices():
    graph = [[(1, -2), (2, -5)], [(2, 1)], [], [(2, 9)]]
    assert longest_path_dag(graph, 0) == [0, -2, -1, -inf]


def test_rejects_cycle():
    with pytest.raises(ValueError):
        longest_path_dag([[(0, 1)]], 0)
