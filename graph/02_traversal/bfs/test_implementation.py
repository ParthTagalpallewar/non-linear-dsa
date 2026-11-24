from .implementation import bfs


def test_cycle_and_neighbor_order():
    graph = {0: [1, 2], 1: [3], 2: [3], 3: [0]}
    assert bfs(graph, 0) == [0, 1, 2, 3]


def test_missing_key_is_a_leaf():
    assert bfs({}, 9) == [9]
