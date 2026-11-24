from random import Random

from .implementation import dinic


def test_flow_equals_exhaustive_cut_capacity():
    rng = Random(19)
    for size in range(2, 7):
        for _ in range(12):
            edges = [
                (u, v, rng.randrange(5))
                for u in range(size)
                for v in range(size)
                if rng.randrange(4) == 0
            ]
            actual = dinic(size, edges, 0, size - 1)
            expected = min(
                sum(w for u, v, w in edges if mask >> u & 1 and not mask >> v & 1)
                for mask in range(1, 1 << (size - 1), 2)
            )
            assert actual == expected


def test_parallel_antiparallel_and_unreachable():
    edges = [(0, 1, 3), (0, 1, 5), (1, 0, 7), (1, 2, 10), (0, 0, 100)]
    assert dinic(3, edges, 0, 2) == 8
    assert dinic(3, [], 0, 2) == 0
