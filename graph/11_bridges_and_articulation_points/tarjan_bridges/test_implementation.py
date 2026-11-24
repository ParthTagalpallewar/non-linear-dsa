from .implementation import tarjan_bridges


def test_parallel_edge_and_self_loop():
    edges = [(0, 1), (1, 0), (1, 2), (2, 2), (2, 3)]
    assert tarjan_bridges(5, edges) == [2, 4]


def test_cycle_and_empty():
    assert tarjan_bridges(3, [(0, 1), (1, 2), (2, 0)]) == []
    assert tarjan_bridges(0, []) == []
