from tree.nodes import BinaryNode

from .implementation import maximum_width


def test_counts_gaps_and_handles_skew():
    left = BinaryNode(2, BinaryNode(4))
    right = BinaryNode(3, None, BinaryNode(5))
    assert maximum_width(BinaryNode(1, left, right)) == 4
    assert maximum_width(BinaryNode(1, left)) == 1
    assert maximum_width(None) == 0
