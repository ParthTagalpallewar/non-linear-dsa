from random import Random

from .implementation import centroid_decomposition


def test_each_decomposition_step_splits_into_balanced_components():
    rng = Random(8)
    for size in range(1, 35):
        graph = [[] for _ in range(size)]
        for child in range(1, size):
            parent = rng.randrange(child)
            graph[parent].append(child)
            graph[child].append(parent)
        ancestor = centroid_decomposition(graph)

        def check(vertices, parent):
            roots = [v for v in vertices if ancestor[v] == parent]
            assert len(roots) == 1
            center = roots[0]
            remaining = vertices - {center}
            while remaining:
                stack = [remaining.pop()]
                component = set(stack)
                for node in stack:
                    for neighbor in graph[node]:
                        if neighbor in remaining:
                            remaining.remove(neighbor)
                            stack.append(neighbor)
                            component.add(neighbor)
                assert 2 * len(component) <= len(vertices)
                check(component, center)

        check(set(range(size)), -1)
    assert centroid_decomposition([]) == []
