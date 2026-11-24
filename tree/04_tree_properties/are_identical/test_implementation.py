from tree.nodes import BinaryNode

from .implementation import are_identical


def test_matching_values_require_matching_shapes():
    assert are_identical(None, None)
    assert are_identical(BinaryNode(2), BinaryNode(2))
    assert not are_identical(
        BinaryNode(2, BinaryNode(2)), BinaryNode(2, None, BinaryNode(2))
    )
