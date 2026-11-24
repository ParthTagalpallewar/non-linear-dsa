from random import Random

from .implementation import tree_isomorphism


def test_relabeling_and_tree_shape_difference():
    rng = Random(4)
    for size in range(1, 34):
        graph = [[] for _ in range(size)]
        renamed = [[] for _ in range(size)]
        labels = rng.sample(range(size), size)
        for child in range(1, size):
            parent = rng.randrange(child)
            graph[child].append(parent)
            graph[parent].append(child)
            renamed[labels[child]].append(labels[parent])
            renamed[labels[parent]].append(labels[child])
        assert tree_isomorphism(graph, renamed)
    assert not tree_isomorphism([[1, 2, 3], [0], [0], [0]], [[1], [0, 2], [1, 3], [2]])
    assert tree_isomorphism([], [])
