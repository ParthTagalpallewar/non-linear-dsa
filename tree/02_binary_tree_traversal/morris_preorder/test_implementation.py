from tree.nodes import BinaryNode

from .implementation import morris_preorder


def test_order_and_thread_restoration():
    leaf = BinaryNode(4)
    root = BinaryNode(1, BinaryNode(2, leaf), BinaryNode(3))
    assert morris_preorder(root) == [1, 2, 4, 3]
    assert leaf.right is None
    assert root.left is not None and root.left.right is None
    assert morris_preorder(None) == []
