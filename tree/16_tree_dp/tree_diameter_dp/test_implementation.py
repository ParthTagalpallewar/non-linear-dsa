from .implementation import tree_diameter_dp


def test_branching_and_empty_trees():
    graph = [[1], [0, 2, 3], [1], [1, 4], [3]]
    assert tree_diameter_dp(graph) == 3
    assert tree_diameter_dp(graph, 4) == 3
    assert tree_diameter_dp([]) == 0
