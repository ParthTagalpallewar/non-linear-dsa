from importlib import import_module
from math import inf
from random import Random

import pytest

from .implementation import johnson


def test_reweight_negative_edge_without_changing_original_distances():
    edges = [(0, 1, 2), (0, 2, 3), (1, 2, -5)]
    assert johnson(3, edges) == [[0, 2, -3], [inf, 0, -5], [inf, inf, 0]]


def test_negative_cycle_in_separate_component_and_empty_graph():
    assert johnson(0, []) == []
    with pytest.raises(ValueError):
        johnson(2, [(1, 1, -1)])


def test_generated_negative_edges_agree_with_floyd_warshall():
    rng = Random(36)
    floyd_warshall = import_module(
        "graph.07_shortest_path.floyd_warshall.implementation"
    ).floyd_warshall
    for size in range(1, 9):
        for _ in range(12):
            potential = [rng.randrange(-10, 11) for _ in range(size)]
            # Every cycle keeps its nonnegative original weight after reweighting.
            edges = [
                (u, v, rng.randrange(6) - potential[u] + potential[v])
                for u in range(size)
                for v in range(size)
                if rng.randrange(4) == 0
            ]
            assert johnson(size, edges) == floyd_warshall(size, edges)
