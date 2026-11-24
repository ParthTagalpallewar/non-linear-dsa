from collections import deque
from random import Random

from .implementation import heavy_light_decomposition


def test_mixed_updates_and_queries_against_explicit_paths():
    rng = Random(351)
    size = 44
    graph = [[] for _ in range(size)]
    for child in range(1, size):
        parent = rng.randrange(child)
        graph[child].append(parent)
        graph[parent].append(child)
    values = [rng.randrange(-4, 5) for _ in graph]
    index = heavy_light_decomposition(graph, values, 3)
    for _ in range(150):
        source, target = rng.randrange(size), rng.randrange(size)
        if rng.randrange(3) == 0:
            values[source] = rng.randrange(-7, 8)
            index.point_set(source, values[source])
        queue = deque([(source, -1, values[source])])
        while queue:
            node, parent, total = queue.popleft()
            if node == target:
                assert index.path_sum(source, target) == total
                break
            queue.extend(
                (v, node, total + values[v]) for v in graph[node] if v != parent
            )
