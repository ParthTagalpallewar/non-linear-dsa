from random import Random

from .implementation import maximum_independent_set


def test_against_subset_enumeration():
    rng = Random(69)
    for size in range(1, 9):
        edges = [(rng.randrange(v), v) for v in range(1, size)]
        graph = [[] for _ in range(size)]
        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)
        expected = max(
            mask.bit_count()
            for mask in range(1 << size)
            if all(not (mask >> u & 1 and mask >> v & 1) for u, v in edges)
        )
        assert maximum_independent_set(graph) == expected
    assert maximum_independent_set([]) == 0
