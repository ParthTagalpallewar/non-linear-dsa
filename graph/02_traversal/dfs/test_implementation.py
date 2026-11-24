from .implementation import dfs


def test_cycle_and_neighbor_order():
    graph = {0: [1, 2], 1: [3], 2: [3], 3: [0]}
    assert dfs(graph, 0) == [0, 1, 3, 2]


def test_missing_key_is_a_leaf():
    assert dfs({}, 9) == [9]
