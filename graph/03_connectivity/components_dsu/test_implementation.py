from .implementation import components_dsu


def test_components_and_isolates():
    result = components_dsu([[1, 1], [0, 0], [2], []])
    assert {frozenset(group) for group in result} == {
        frozenset({0, 1}),
        frozenset({2}),
        frozenset({3}),
    }


def test_empty_graph():
    assert components_dsu([]) == []
