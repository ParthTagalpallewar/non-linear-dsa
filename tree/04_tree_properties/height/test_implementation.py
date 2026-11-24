from tree.nodes import BinaryNode

from .implementation import height


def test_empty_singleton_and_branch():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4)), BinaryNode(3))
    assert height(root) == 2
    assert height(BinaryNode(1)) == 0
    assert height(None) == -1
