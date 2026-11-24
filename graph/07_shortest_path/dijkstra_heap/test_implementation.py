from math import inf

import pytest

from .implementation import dijkstra_heap


def test_improved_candidate_and_isolate():
    assert dijkstra_heap([[(1, 8), (2, 1)], [], [(1, 2)], []], 0) == [0, 3, 1, inf]


def test_rejects_negative_edges():
    with pytest.raises(ValueError):
        dijkstra_heap([[(0, -1)]], 0)
