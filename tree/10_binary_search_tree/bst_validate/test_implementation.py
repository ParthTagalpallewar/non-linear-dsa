from tree.nodes import BinaryNode

from .implementation import bst_validate


def test_rejects_deep_ancestor_violation_and_duplicate():
    assert bst_validate(None)
    assert bst_validate(BinaryNode(4, BinaryNode(2), BinaryNode(6)))
    assert not bst_validate(BinaryNode(4, BinaryNode(2, None, BinaryNode(5))))
    assert not bst_validate(BinaryNode(4, BinaryNode(4)))
