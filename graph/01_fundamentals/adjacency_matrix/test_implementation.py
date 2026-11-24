from .implementation import adjacency_matrix


def test_directed_edge_and_loop():
    assert adjacency_matrix(2, [(0, 1), (1, 1)], directed=True) == [
        [False, True],
        [False, True],
    ]


def test_undirected_edge_is_symmetric():
    assert adjacency_matrix(2, [(0, 1)]) == [[False, True], [True, False]]
