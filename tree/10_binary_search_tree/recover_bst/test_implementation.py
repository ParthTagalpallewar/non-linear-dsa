from tree.nodes import BinaryNode

from .implementation import recover_bst


def test_adjacent_and_nonadjacent_swaps():
    for left, middle, right in [(2, 1, 3), (3, 2, 1)]:
        tree = BinaryNode(middle, BinaryNode(left), BinaryNode(right))
        recover_bst(tree)
        assert (tree.left.value, tree.value, tree.right.value) == (1, 2, 3)
    recover_bst(None)
