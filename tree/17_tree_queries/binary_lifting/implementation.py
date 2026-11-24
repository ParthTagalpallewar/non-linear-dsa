"""Binary Lifting."""

from tree.queries import BinaryLifting


def binary_lifting(graph: list[list[int]], root: int = 0) -> BinaryLifting:
    """Build a table of ancestors at powers-of-two distances."""
    return BinaryLifting(graph, root)
