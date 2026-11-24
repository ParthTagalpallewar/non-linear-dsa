from .implementation import bidirectional_bfs


def test_search_switches_to_smaller_frontier():
    graph = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1, 4], 4: [3]}
    assert bidirectional_bfs(graph, 0, 4) == 3


def test_disconnected_and_same_vertex():
    assert bidirectional_bfs({}, 0, 1) is None
    assert bidirectional_bfs({}, 0, 0) == 0
