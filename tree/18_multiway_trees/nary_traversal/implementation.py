"""N-ary Tree Traversal."""

from collections.abc import Iterator

from tree.nodes import NaryNode


def nary_traversal(root: NaryNode | None) -> Iterator[int]:
    """Yield the nodes of an ordered N-ary tree in preorder."""
    stack = [root] if root is not None else []
    while stack:
        node = stack.pop()
        yield node.value
        stack.extend(reversed(node.children))
