from math import inf

import pytest

from .implementation import zero_one_bfs


def test_free_route_beats_direct_edge():
    assert zero_one_bfs([[(1, 1), (2, 0)], [], [(1, 0)], []], 0) == [
        0,
        0,
        0,
        inf,
    ]


def test_rejects_weight_above_one():
    with pytest.raises(ValueError):
        zero_one_bfs([[(0, 2)]], 0)
