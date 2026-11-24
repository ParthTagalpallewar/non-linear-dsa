"""Ancestor and Descendant Queries."""

from tree.nodes import BinaryNode


def ancestor_queries(
    root: BinaryNode | None, queries: list[tuple[BinaryNode, BinaryNode]]
) -> list[bool]:
    """Answer whether the first node contains the second in its subtree."""
    enter: dict[BinaryNode, int] = {}
    leave: dict[BinaryNode, int] = {}
    clock = 0
    stack = [(root, False)]
    while stack:
        node, exiting = stack.pop()
        if node is None:
            continue
        if exiting:
            leave[node] = clock
        else:
            enter[node] = clock
            clock += 1
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
    return [
        ancestor in enter
        and descendant in enter
        and enter[ancestor] <= enter[descendant] < leave[ancestor]
        for ancestor, descendant in queries
    ]
