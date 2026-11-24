from tree.queries import BinaryLifting

from .implementation import lca_binary_lifting


def test_split_pair_and_ancestor_pair():
    index = BinaryLifting([[1, 2], [0, 3, 4], [0], [1], [1]])
    assert lca_binary_lifting(index, 3, 4) == 1
    assert lca_binary_lifting(index, 3, 2) == 0
    assert lca_binary_lifting(index, 3, 1) == 1
