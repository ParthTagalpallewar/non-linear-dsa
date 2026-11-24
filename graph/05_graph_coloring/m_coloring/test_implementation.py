from .implementation import m_coloring


def test_triangle_uses_three_colors():
    graph = [[1, 2], [0, 2], [0, 1]]
    assert m_coloring(graph, 2) is None
    assert m_coloring(graph, 3) == [0, 1, 2]


def test_loop_empty_and_empty_palette():
    assert m_coloring([[0]], 3) is None
    assert m_coloring([], 0) == []
    assert m_coloring([[]], 0) is None
