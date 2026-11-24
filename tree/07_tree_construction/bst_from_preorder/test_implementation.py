import pytest

from .implementation import bst_from_preorder


def test_bounds_close_a_subtree():
    root = bst_from_preorder([8, 5, 1, 7, 10, 12])
    assert root is not None and root.left is not None and root.right is not None
    assert root.left.right is not None and root.left.right.value == 7
    assert root.right.right is not None and root.right.right.value == 12


def test_invalid_order_duplicates_and_empty():
    assert bst_from_preorder([]) is None
    for values in ([8, 10, 5], [2, 2]):
        with pytest.raises(ValueError):
            bst_from_preorder(values)
