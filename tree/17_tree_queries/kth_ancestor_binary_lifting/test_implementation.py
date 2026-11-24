from tree.queries import BinaryLifting

from .implementation import kth_ancestor_binary_lifting


def test_mixed_binary_jumps():
    graph = [[1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5]]
    index = BinaryLifting(graph)
    assert kth_ancestor_binary_lifting(index, 6, 5) == 1
    assert kth_ancestor_binary_lifting(index, 6, 0) == 6
    assert kth_ancestor_binary_lifting(index, 2, 3) is None
