from tree.nodes import BinaryNode

from .implementation import count_leaves


def test_empty_singleton_and_branch():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4)), BinaryNode(3))
    assert count_leaves(root) == 2
    assert count_leaves(BinaryNode(1)) == 1
    assert count_leaves(None) == 0
