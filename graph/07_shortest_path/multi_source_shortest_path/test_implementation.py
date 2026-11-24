from math import inf

from .implementation import multi_source_shortest_path


def test_nearest_source_wins_and_unreachable_remains_infinite():
    graph = [[(2, 8)], [(2, 4)], [], []]
    assert multi_source_shortest_path(graph, [0, 1, 1]) == [0, 0, 4, inf]


def test_no_sources():
    assert multi_source_shortest_path([[]], []) == [inf]
