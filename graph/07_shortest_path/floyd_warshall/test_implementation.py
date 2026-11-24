from math import inf

import pytest

from .implementation import floyd_warshall


def test_all_pairs_parallel_edges_and_negative_edge():
    edges = [(0, 1, 9), (0, 1, 2), (1, 2, -3)]
    assert floyd_warshall(3, edges) == [[0, 2, -1], [inf, 0, -3], [inf, inf, 0]]


def test_negative_cycle_and_empty_graph():
    assert floyd_warshall(0, []) == []
    with pytest.raises(ValueError):
        floyd_warshall(1, [(0, 0, -1)])
