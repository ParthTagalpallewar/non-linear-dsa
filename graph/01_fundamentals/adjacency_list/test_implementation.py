from .implementation import adjacency_list


def test_undirected_loop_and_isolated_vertex():
    assert adjacency_list(3, [(0, 1), (1, 1)]) == [[1], [0, 1, 1], []]


def test_directed_preserves_parallel_edges():
    assert adjacency_list(2, [(0, 1), (0, 1)], directed=True) == [[1, 1], []]


def test_empty_graph():
    assert adjacency_list(0, []) == []
