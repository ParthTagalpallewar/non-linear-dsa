from tree.nodes import BinaryNode

from .implementation import tree_to_doubly_linked_list


def test_links_in_both_directions():
    first, last = BinaryNode(1), BinaryNode(3)
    root = BinaryNode(2, first, last)
    assert tree_to_doubly_linked_list(root) is first
    assert first.left is None and first.right is root
    assert root.left is first and root.right is last
    assert last.left is root and last.right is None
    assert tree_to_doubly_linked_list(None) is None
