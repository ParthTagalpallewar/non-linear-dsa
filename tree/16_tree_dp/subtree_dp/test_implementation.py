from .implementation import subtree_dp


def test_aggregates_each_child_once():
    graph = [[1], [0, 2, 3], [1], [1]]
    assert subtree_dp(graph, [1, 2, -2, 4]) == [5, 4, -2, 4]
    assert subtree_dp([], []) == []
