from tree.nodes import BinaryNode

from .implementation import morris_inorder


def test_order_and_thread_restoration():
    leaf = BinaryNode(4)
    root = BinaryNode(1, BinaryNode(2, leaf), BinaryNode(3))
    assert morris_inorder(root) == [4, 2, 1, 3]
    assert leaf.right is None
    assert root.left is not None and root.left.right is None
    assert morris_inorder(None) == []
