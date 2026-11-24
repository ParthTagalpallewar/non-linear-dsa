from .implementation import path_queries


def test_includes_lca_once_and_handles_negative_values():
    graph = [[1, 2], [0, 3, 4], [0], [1], [1]]
    assert path_queries(graph, [8, 2, -5, 4, 1], [(3, 2), (1, 4), (0, 0)]) == [
        9,
        3,
        8,
    ]
    assert path_queries([], [], []) == []
