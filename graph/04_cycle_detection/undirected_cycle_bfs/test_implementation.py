from .implementation import undirected_cycle_bfs


def test_forest_and_disconnected_cycle():
    assert not undirected_cycle_bfs([[1], [0], []])
    assert undirected_cycle_bfs([[], [2, 3], [1, 3], [2, 1]])


def test_loop_and_parallel_edges():
    assert undirected_cycle_bfs([[0]])
    assert undirected_cycle_bfs([[1, 1], [0, 0]])
