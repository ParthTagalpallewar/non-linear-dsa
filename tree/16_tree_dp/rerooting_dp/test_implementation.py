from collections import deque
from random import Random

from .implementation import rerooting_dp


def test_against_bfs_from_each_vertex():
    rng = Random(23)
    for size in range(1, 30):
        graph = [[] for _ in range(size)]
        for vertex in range(1, size):
            parent = rng.randrange(vertex)
            graph[parent].append(vertex)
            graph[vertex].append(parent)
        expected = []
        for source in range(size):
            queue = deque([(source, -1, 0)])
            total = 0
            while queue:
                vertex, parent, depth = queue.popleft()
                total += depth
                queue.extend(
                    (v, vertex, depth + 1) for v in graph[vertex] if v != parent
                )
            expected.append(total)
        assert rerooting_dp(graph, size // 2) == expected
    assert rerooting_dp([]) == []
