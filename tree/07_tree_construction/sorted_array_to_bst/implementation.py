"""Convert Sorted Array to Balanced BST."""

from itertools import pairwise

from tree.nodes import BinaryNode


def sorted_array_to_bst(values: list[int]) -> BinaryNode | None:
    """Build a height-balanced strict BST from strictly increasing keys."""
    if any(left >= right for left, right in pairwise(values)):
        raise ValueError("keys must be strictly increasing")

    def build(left: int, right: int) -> BinaryNode | None:
        if left >= right:
            return None
        middle = (left + right) // 2
        return BinaryNode(values[middle], build(left, middle), build(middle + 1, right))

    return build(0, len(values))
