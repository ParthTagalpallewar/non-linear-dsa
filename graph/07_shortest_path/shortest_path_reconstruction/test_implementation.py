from .implementation import shortest_path_reconstruction


def test_improvements_change_parent():
    graph = [[(1, 10), (2, 2)], [], [(1, 3)], []]
    assert shortest_path_reconstruction(graph, 0, 1) == [0, 2, 1]
    assert shortest_path_reconstruction(graph, 0, 3) == []


def test_source_is_its_own_route():
    assert shortest_path_reconstruction([[(0, 0)]], 0, 0) == [0]
