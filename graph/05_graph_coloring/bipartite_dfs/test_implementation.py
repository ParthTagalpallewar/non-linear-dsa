from .implementation import bipartite_dfs


def test_square_and_disconnected_odd_cycle():
    assert bipartite_dfs([[1, 3], [0, 2], [1, 3], [0, 2], []])
    assert not bipartite_dfs([[], [2, 3], [1, 3], [1, 2]])


def test_empty_and_loop():
    assert bipartite_dfs([])
    assert not bipartite_dfs([[0]])
