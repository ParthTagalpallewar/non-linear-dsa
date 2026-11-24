from tree.nodes import BinaryNode

from .implementation import root_to_leaf_path_sum


def test_negative_leaf_and_internal_target():
    root = BinaryNode(3, BinaryNode(-2))
    assert root_to_leaf_path_sum(root, 1)
    assert not root_to_leaf_path_sum(root, 3)
    assert not root_to_leaf_path_sum(None, 0)
