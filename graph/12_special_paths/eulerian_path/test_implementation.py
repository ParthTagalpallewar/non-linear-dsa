from collections import Counter

from .implementation import eulerian_path


def test_each_parallel_edge_and_loop_is_consumed_once():
    edges = [(0, 1), (1, 0), (1, 1)]
    route = eulerian_path(3, edges)
    assert route is not None
    assert route[0] == route[-1]
    assert Counter(
        tuple(sorted(edge)) for edge in zip(route, route[1:], strict=False)
    ) == Counter(tuple(sorted(edge)) for edge in edges)


def test_disconnected_and_odd_endpoints():
    assert eulerian_path(4, [(0, 0), (3, 3)]) is None
    assert eulerian_path(2, [(0, 1)]) == [0, 1]
    assert eulerian_path(0, []) == []
