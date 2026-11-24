"""Convert Binary Tree to Doubly Linked List."""

from tree.nodes import BinaryNode


def tree_to_doubly_linked_list(root: BinaryNode | None) -> BinaryNode | None:
    """Return the head of an in-place, noncircular inorder list."""
    stack: list[BinaryNode] = []
    head = previous = None
    current = root
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        next_subtree = current.right
        current.left = previous
        if previous is None:
            head = current
        else:
            previous.right = current
        previous = current
        current = next_subtree
    if previous is not None:
        previous.right = None
    return head
