"""N-ary Tree Node."""

from collections.abc import Iterable

from tree.nodes import NaryNode


def nary_node(value: int, children: Iterable[NaryNode] = ()) -> NaryNode:
    """Create a n-ary tree node from a value and optional children."""
    return NaryNode(value, list(children))
