from random import Random

from .implementation import hopcroft_karp


def test_augmenting_path_reassigns_previous_pair():
    assert hopcroft_karp([[0, 1], [0], []], 3) == [(0, 1), (1, 0)]
    assert hopcroft_karp([], 2) == []


def test_small_graphs_against_exhaustive_search():
    rng = Random(22)
    for size in range(1, 6):
        for _ in range(10):
            graph = [
                [right for right in range(size) if rng.randrange(2)]
                for _ in range(size)
            ]

            def best(left: int, used: set[int]) -> int:
                if left == size:
                    return 0
                return max(
                    [best(left + 1, used)]
                    + [
                        1 + best(left + 1, used | {right})
                        for right in graph[left]
                        if right not in used
                    ]
                )

            pairs = hopcroft_karp(graph, size)
            assert all(right in graph[left] for left, right in pairs)
            assert len({left for left, _ in pairs}) == len(pairs)
            assert len({right for _, right in pairs}) == len(pairs)
            assert len(pairs) == best(0, set())
