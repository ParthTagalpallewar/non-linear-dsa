"""Two Sum in a BST."""

from tree.nodes import BinaryNode


def bst_two_sum(root: BinaryNode | None, target: int) -> bool:
    """Return whether distinct nodes have values that sum to target."""
    seen = set()
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        if target - node.value in seen:
            return True
        seen.add(node.value)
        stack.extend((node.left, node.right))
    return False
