from tree.nodes import BinaryNode

from .implementation import lca_binary_tree


def test_duplicate_values_and_absent_node():
    first = BinaryNode(2)
    second = BinaryNode(2)
    root = BinaryNode(1, first, second)
    assert lca_binary_tree(root, first, second) is root
    assert lca_binary_tree(root, first, first) is first
    assert lca_binary_tree(root, first, BinaryNode(2)) is None
