from itertools import combinations
from random import Random

from graph.disjoint_set import DisjointSet

from .implementation import prim_array


def test_disconnected_parallel_and_negative_edges():
    edges = [(0, 1, 4), (0, 1, -2), (1, 2, 1), (0, 2, 8), (3, 3, -9)]
    forest = prim_array(5, edges)
    assert len(forest) == 2
    assert sum(weight for _, _, weight in forest) == -1
    assert prim_array(0, []) == []


def test_connected_graphs_against_exhaustive_minimum():
    rng = Random(34)
    for _ in range(8):
        edges = [(u, v, rng.randrange(-5, 6)) for u, v in combinations(range(4), 2)]
        tree = prim_array(4, edges)
        assert len(tree) == 3
        actual = DisjointSet(4)
        assert all(actual.union(u, v) for u, v, _ in tree)
        assert all(
            edge in edges or (edge[1], edge[0], edge[2]) in edges for edge in tree
        )
        candidate_weights = []
        for candidate in combinations(edges, 3):
            groups = DisjointSet(4)
            if all(groups.union(u, v) for u, v, _ in candidate):
                candidate_weights.append(sum(w for _, _, w in candidate))
        assert sum(w for _, _, w in tree) == min(candidate_weights)
