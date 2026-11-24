from tree.nodes import BinaryNode

from .implementation import ancestor_queries


def test_intervals_with_siblings_and_absent_identity():
    left, right = BinaryNode(2), BinaryNode(2)
    root = BinaryNode(1, left, right)
    queries = [(root, left), (left, right), (right, right), (root, BinaryNode(2))]
    assert ancestor_queries(root, queries) == [True, False, True, False]
    assert ancestor_queries(None, queries) == [False] * 4
