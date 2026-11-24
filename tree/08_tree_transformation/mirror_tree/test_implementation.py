from tree.nodes import BinaryNode

from .implementation import mirror_tree


def test_orientation_and_mutation_contract():
    child = BinaryNode(2, BinaryNode(3))
    root = BinaryNode(1, child)
    result = mirror_tree(root)
    assert result is not None and result.left is None
    assert result.right is not None and result.right.left is None
    assert result.right.right is not None and result.right.right.value == 3
    assert result is not root
    assert root.left is child
    assert mirror_tree(None) is None
