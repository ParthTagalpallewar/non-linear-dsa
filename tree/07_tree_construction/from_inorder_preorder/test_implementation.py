import pytest

from .implementation import from_inorder_preorder


def test_reconstructs_missing_child():
    root = from_inorder_preorder([4, 2, 1, 3], [1, 2, 4, 3])
    assert root is not None and root.value == 1
    assert root.left is not None and root.left.value == 2
    assert root.left.left is not None and root.left.left.value == 4
    assert root.left.right is None
    assert root.right is not None and root.right.value == 3


def test_empty_and_inconsistent_input():
    assert from_inorder_preorder([], []) is None
    with pytest.raises(ValueError):
        from_inorder_preorder([1, 2], [1, 3])
