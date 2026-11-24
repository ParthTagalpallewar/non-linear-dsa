from random import Random

from tree.queries import BinaryLifting, EulerLCA

from .implementation import lca_euler_sparse_table


def test_against_binary_lifting_for_all_pairs():
    rng = Random(111)
    for size in range(1, 24):
        graph = [[] for _ in range(size)]
        for child in range(1, size):
            parent = rng.randrange(child)
            graph[parent].append(child)
            graph[child].append(parent)
        index = EulerLCA(graph, size // 2)
        other = BinaryLifting(graph, size // 2)
        for left in range(size):
            for right in range(size):
                assert lca_euler_sparse_table(index, left, right) == other.lca(
                    left, right
                )
