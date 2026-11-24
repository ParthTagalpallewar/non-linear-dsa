import pytest

from .implementation import full_from_preorder_postorder


def test_full_tree_and_empty():
    root = full_from_preorder_postorder([1, 2, 4, 5, 3], [4, 5, 2, 3, 1])
    assert root is not None and root.left is not None and root.right is not None
    assert root.left.left is not None and root.left.left.value == 4
    assert root.right.value == 3
    assert full_from_preorder_postorder([], []) is None


def test_rejects_ambiguous_single_child():
    with pytest.raises(ValueError):
        full_from_preorder_postorder([1, 2], [2, 1])
