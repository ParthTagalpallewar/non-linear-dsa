from .implementation import subtree_queries


def test_subtrees_are_contiguous():
    graph = [[1, 2], [0, 3, 4], [0], [1], [1]]
    assert subtree_queries(graph, [1, 2, 3, 4, 5], [1, 0, 2]) == [11, 15, 3]
    assert subtree_queries([], [], []) == []
