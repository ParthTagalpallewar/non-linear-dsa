from random import Random

from .implementation import tarjan_bridges


def test_parallel_edge_and_self_loop():
    edges = [(0, 1), (1, 0), (1, 2), (2, 2), (2, 3)]
    assert tarjan_bridges(5, edges) == [2, 4]


def test_cycle_and_empty():
    assert tarjan_bridges(3, [(0, 1), (1, 2), (2, 0)]) == []
    assert tarjan_bridges(0, []) == []


def test_against_removing_every_physical_edge():
    rng = Random(53)

    def count_components(size: int, edges: list[tuple[int, int]]) -> int:
        graph: list[list[int]] = [[] for _ in range(size)]
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)
        unseen = set(range(size))
        count = 0
        while unseen:
            count += 1
            pending = [unseen.pop()]
            for vertex in pending:
                for target in graph[vertex]:
                    if target in unseen:
                        unseen.remove(target)
                        pending.append(target)
        return count

    for size in range(1, 8):
        for _ in range(12):
            edges = [(rng.randrange(size), rng.randrange(size)) for _ in range(12)]
            before = count_components(size, edges)
            expected = [
                edge
                for edge in range(len(edges))
                if count_components(size, edges[:edge] + edges[edge + 1 :]) > before
            ]
            assert tarjan_bridges(size, edges) == expected
