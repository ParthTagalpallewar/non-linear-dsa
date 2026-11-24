from math import inf

from .implementation import a_star


def test_admissible_inconsistent_heuristic_reopens_vertex():
    graph = [[(1, 4), (2, 2)], [(3, 5)], [(1, 1)], []]
    assert a_star(graph, 0, 3, [0, 0, 6, 0].__getitem__) == (8, [0, 2, 1, 3])


def test_empty_route_and_unreachable_goal():
    assert a_star([[], []], 0, 0, lambda _: 0) == (0, [0])
    assert a_star([[], []], 0, 1, lambda _: 0) == (inf, [])
