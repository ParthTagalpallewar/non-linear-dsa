from .implementation import bipartite_bfs


def test_square_and_disconnected_odd_cycle():
    assert bipartite_bfs([[1, 3], [0, 2], [1, 3], [0, 2], []])
    assert not bipartite_bfs([[], [2, 3], [1, 3], [1, 2]])


def test_empty_and_loop():
    assert bipartite_bfs([])
    assert not bipartite_bfs([[0]])
