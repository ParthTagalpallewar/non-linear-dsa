import pytest

from tree.nodes import BinaryNode

from .implementation import kth_largest


def test_rank_and_out_of_bounds():
    root = BinaryNode(4, BinaryNode(2), BinaryNode(6, right=BinaryNode(8)))
    assert kth_largest(root, 2) == 6
    for rank in (0, 5):
        with pytest.raises(ValueError):
            kth_largest(root, rank)
