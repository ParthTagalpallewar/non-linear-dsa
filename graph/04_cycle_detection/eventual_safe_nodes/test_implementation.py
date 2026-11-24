from .implementation import eventual_safe_nodes


def test_branch_to_cycle_makes_start_unsafe():
    assert eventual_safe_nodes([[1, 2], [1], [3], []]) == [2, 3]


def test_isolated_vertices_and_empty_graph():
    assert eventual_safe_nodes([[], [1], []]) == [0, 2]
    assert eventual_safe_nodes([]) == []
