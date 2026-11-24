from math import inf

import pytest

from .implementation import bellman_ford


def test_negative_edge_and_unreachable_negative_cycle():
    assert bellman_ford(4, [(0, 1, 2), (1, 2, -3), (3, 3, -1)], 0) == [
        0,
        2,
        -1,
        inf,
    ]


def test_reachable_negative_cycle():
    with pytest.raises(ValueError):
        bellman_ford(2, [(0, 1, 1), (1, 1, -1)], 0)
