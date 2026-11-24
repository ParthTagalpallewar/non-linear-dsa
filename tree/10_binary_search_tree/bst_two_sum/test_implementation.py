from tree.nodes import BinaryNode

from .implementation import bst_two_sum


def test_cross_subtree_pair_and_no_reused_node():
    root = BinaryNode(4, BinaryNode(2), BinaryNode(8))
    assert bst_two_sum(root, 10)
    assert not bst_two_sum(root, 16)
    assert not bst_two_sum(None, 0)
