from math import inf

import pytest

from .implementation import johnson


def test_reweight_negative_edge_without_changing_original_distances():
    edges = [(0, 1, 2), (0, 2, 3), (1, 2, -5)]
    assert johnson(3, edges) == [[0, 2, -3], [inf, 0, -5], [inf, inf, 0]]


def test_negative_cycle_in_separate_component_and_empty_graph():
    assert johnson(0, []) == []
    with pytest.raises(ValueError):
        johnson(2, [(1, 1, -1)])
