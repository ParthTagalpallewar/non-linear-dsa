from tree.nodes import BinaryNode

from .implementation import lca_bst


def test_split_and_missing_key():
    root = BinaryNode(2, BinaryNode(1), BinaryNode(3))
    assert lca_bst(root, 1, 3) is root
    assert lca_bst(root, 1, 1) is root.left
    assert lca_bst(root, 1, 4) is None
