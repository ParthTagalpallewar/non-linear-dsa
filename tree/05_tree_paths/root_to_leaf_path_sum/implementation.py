"""Root-to-Leaf Path Sum."""

from tree.nodes import BinaryNode


def root_to_leaf_path_sum(root: BinaryNode | None, target: int) -> bool:
    """Return whether any complete root-to-leaf route sums to target."""
    if root is None:
        return False
    remaining = target - root.value
    if root.left is None and root.right is None:
        return remaining == 0
    return root_to_leaf_path_sum(root.left, remaining) or root_to_leaf_path_sum(
        root.right, remaining
    )
