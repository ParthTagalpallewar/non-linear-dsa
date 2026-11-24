from .implementation import directed_cycle_dfs


def test_shared_descendant_and_back_edge():
    assert not directed_cycle_dfs([[1, 2], [2], []])
    assert directed_cycle_dfs([[], [2], [1]])


def test_self_loop_and_empty():
    assert directed_cycle_dfs([[0]])
    assert not directed_cycle_dfs([])
