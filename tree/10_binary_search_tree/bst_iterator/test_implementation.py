from tree.nodes import BinaryNode

from .implementation import bst_iterator


def test_lazy_inorder_resume():
    root = BinaryNode(4, BinaryNode(2), BinaryNode(6))
    stream = bst_iterator(root)
    assert next(stream) == 2
    assert list(stream) == [4, 6]
    assert list(bst_iterator(None)) == []
