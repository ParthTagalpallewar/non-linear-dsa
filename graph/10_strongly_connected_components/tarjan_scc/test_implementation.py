from random import Random

from .implementation import tarjan_scc


def test_two_components_and_isolate():
    graph = [[1], [0, 2], [3], [2], []]
    result = tarjan_scc(graph)
    assert sorted(sorted(group) for group in result) == [[0, 1], [2, 3], [4]]


def test_empty_and_self_loop():
    assert tarjan_scc([]) == []
    assert tarjan_scc([[0]]) == [[0]]


def test_random_graphs_against_mutual_reachability():
    rng = Random(122)
    for size in range(1, 8):
        for _ in range(8):
            graph = [
                [v for v in range(size) if rng.randrange(3) == 0] for _ in range(size)
            ]
            reach = []
            for start in range(size):
                seen = {start}
                queue = [start]
                for vertex in queue:
                    for target in graph[vertex]:
                        if target not in seen:
                            seen.add(target)
                            queue.append(target)
                reach.append(seen)
            expected = {
                frozenset(v for v in reach[u] if u in reach[v]) for u in range(size)
            }
            assert {frozenset(group) for group in tarjan_scc(graph)} == expected
