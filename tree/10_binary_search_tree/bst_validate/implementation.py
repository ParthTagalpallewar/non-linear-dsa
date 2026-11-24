"""BST Validation."""

from tree.nodes import BinaryNode


def bst_validate(root: BinaryNode | None) -> bool:
    """Check strict BST ordering against all ancestor bounds."""
    stack: list[tuple[BinaryNode | None, int | None, int | None]] = [(root, None, None)]
    while stack:
        node, low, high = stack.pop()
        if node is None:
            continue
        if (low is not None and node.value <= low) or (
            high is not None and node.value >= high
        ):
            return False
        stack.append((node.right, node.value, high))
        stack.append((node.left, low, node.value))
    return True
