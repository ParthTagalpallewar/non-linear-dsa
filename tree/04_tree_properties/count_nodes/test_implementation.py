from tree.nodes import BinaryNode

from .implementation import count_nodes


def test_empty_singleton_and_branch():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4)), BinaryNode(3))
    assert count_nodes(root) == 4
    assert count_nodes(BinaryNode(1)) == 1
    assert count_nodes(None) == 0
