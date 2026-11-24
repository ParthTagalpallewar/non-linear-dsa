from math import inf

import pytest

from .implementation import dag_shortest_path


def test_negative_edge_and_disconnected_vertex():
    graph = [[(1, 2), (2, 1)], [(2, -3)], [], [(2, -100)]]
    assert dag_shortest_path(graph, 0) == [0, 2, -1, inf]


def test_rejects_cycle():
    with pytest.raises(ValueError):
        dag_shortest_path([[(0, -1)]], 0)
