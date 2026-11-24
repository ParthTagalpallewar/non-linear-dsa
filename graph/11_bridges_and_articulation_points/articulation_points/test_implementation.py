from .implementation import articulation_points


def test_parallel_edge_and_self_loop():
    edges = [(0, 1), (1, 0), (1, 2), (2, 2), (2, 3)]
    assert articulation_points(5, edges) == [1, 2]


def test_cycle_and_empty():
    assert articulation_points(3, [(0, 1), (1, 2), (2, 0)]) == []
    assert articulation_points(0, []) == []
