from collections import Counter

from .implementation import fleury


def test_postpones_an_available_bridge():
    edges = [(0, 3), (0, 1), (1, 2), (2, 0)]
    route = fleury(4, edges)
    assert route == [0, 1, 2, 0, 3]
    steps = zip(route, route[1:], strict=False)
    assert Counter(tuple(sorted(pair)) for pair in steps) == Counter(
        tuple(sorted(edge)) for edge in edges
    )


def test_handles_parallel_edges_and_disconnected_components():
    assert fleury(2, [(0, 1), (0, 1)]) == [0, 1, 0]
    assert fleury(2, [(0, 0), (1, 1)]) is None
