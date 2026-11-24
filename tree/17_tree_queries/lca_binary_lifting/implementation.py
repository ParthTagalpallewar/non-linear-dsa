"""LCA Using Binary Lifting."""

from tree.queries import BinaryLifting


def lca_binary_lifting(index: BinaryLifting, left: int, right: int) -> int:
    """Return the lowest common ancestor using an existing jump table."""
    return index.lca(left, right)
