from tree.nodes import BinaryNode

from .implementation import is_balanced


def test_height_check_and_empty_tree():
    assert is_balanced(None)
    assert is_balanced(BinaryNode(1, BinaryNode(2), BinaryNode(3)))
    assert not is_balanced(BinaryNode(1, BinaryNode(2, BinaryNode(3))))
