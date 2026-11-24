from random import Random

from .implementation import dsu_on_tree


def test_matches_explicit_subtree_sets():
    rng = Random(71)
    for size in range(1, 35):
        graph = [[] for _ in range(size)]
        parent = [-1]
        for vertex in range(1, size):
            above = rng.randrange(vertex)
            parent.append(above)
            graph[above].append(vertex)
            graph[vertex].append(above)
        colors = [rng.randrange(8) for _ in graph]
        expected = [{value} for value in colors]
        for vertex in reversed(range(1, size)):
            expected[parent[vertex]].update(expected[vertex])
        assert dsu_on_tree(graph, colors) == [len(group) for group in expected]
    assert dsu_on_tree([], []) == []
