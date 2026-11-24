from .implementation import grid_dfs


def test_obstacle_and_visit_order():
    assert grid_dfs([[0, 0], [0, 1]], (0, 0)) == [(0, 0), (0, 1), (1, 0)]


def test_empty_or_blocked_start():
    assert grid_dfs([], (0, 0)) == []
    assert grid_dfs([[1]], (0, 0)) == []
