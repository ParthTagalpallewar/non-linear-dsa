from tree.nodes import BinaryNode

from .implementation import flatten_preorder


def test_reuses_nodes_in_preorder_and_clears_left_links():
    leaf = BinaryNode(4)
    left = BinaryNode(2, leaf)
    right = BinaryNode(3)
    root = BinaryNode(1, left, right)
    assert flatten_preorder(root) is root
    for node in (root, left, leaf, right):
        assert root is node and root.left is None
        root = root.right
    assert root is None
    assert flatten_preorder(None) is None
