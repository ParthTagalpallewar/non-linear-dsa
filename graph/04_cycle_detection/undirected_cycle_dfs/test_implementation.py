from .implementation import undirected_cycle_dfs


def test_forest_and_disconnected_cycle():
    assert not undirected_cycle_dfs([[1], [0], []])
    assert undirected_cycle_dfs([[], [2, 3], [1, 3], [2, 1]])


def test_loop_and_parallel_edges():
    assert undirected_cycle_dfs([[0]])
    assert undirected_cycle_dfs([[1, 1], [0, 0]])
