from tree.nodes import BinaryNode

from .implementation import is_symmetric


def test_mirror_and_value_mismatch():
    root = BinaryNode(
        1, BinaryNode(2, BinaryNode(3)), BinaryNode(2, None, BinaryNode(3))
    )
    assert is_symmetric(root)
    assert root.right is not None
    root.right.value = 9
    assert not is_symmetric(root)
    assert is_symmetric(None)
