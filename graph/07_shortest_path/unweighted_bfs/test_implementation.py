from math import inf

from .implementation import unweighted_bfs


def test_shortcut_beats_indirect_path():
    assert unweighted_bfs([[1, 2], [2], [0], []], 0) == [0, 1, 1, inf]


def test_loop_has_zero_distance_to_source():
    assert unweighted_bfs([[0]], 0) == [0]
