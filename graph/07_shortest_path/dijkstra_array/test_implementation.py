from math import inf

import pytest

from .implementation import dijkstra_array


def test_improved_candidate_and_isolate():
    assert dijkstra_array([[(1, 8), (2, 1)], [], [(1, 2)], []], 0) == [0, 3, 1, inf]


def test_rejects_negative_edges():
    with pytest.raises(ValueError):
        dijkstra_array([[(0, -1)]], 0)
