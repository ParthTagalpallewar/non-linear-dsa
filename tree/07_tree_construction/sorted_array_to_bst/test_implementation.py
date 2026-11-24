import pytest

from .implementation import sorted_array_to_bst


def test_balanced_and_empty():
    root = sorted_array_to_bst([1, 2, 3, 4, 5])
    assert root is not None and root.value == 3
    assert root.left is not None and root.left.value == 2
    assert root.right is not None and root.right.value == 5
    assert sorted_array_to_bst([]) is None
    assert sorted_array_to_bst([8]).value == 8


def test_rejects_duplicates_and_unsorted_keys():
    for values in ([1, 1], [3, 2]):
        with pytest.raises(ValueError):
            sorted_array_to_bst(values)
