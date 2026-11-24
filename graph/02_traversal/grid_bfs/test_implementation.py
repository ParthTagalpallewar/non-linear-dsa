from .implementation import grid_bfs


def test_obstacle_and_visit_order():
    assert grid_bfs([[0, 0], [0, 1]], (0, 0)) == [(0, 0), (1, 0), (0, 1)]


def test_empty_or_blocked_start():
    assert grid_bfs([], (0, 0)) == []
    assert grid_bfs([[1]], (0, 0)) == []
