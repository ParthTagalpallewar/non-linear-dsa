"""Serialization and Deserialization Using BFS."""

from collections import deque

from tree.nodes import BinaryNode


def serialize_bfs(root: BinaryNode | None) -> str:
    """Encode level-order values and explicit nulls, separated by commas."""
    pending = deque([root])
    tokens = []
    while pending:
        node = pending.popleft()
        if node is None:
            tokens.append("#")
        else:
            tokens.append(str(node.value))
            pending.extend((node.left, node.right))
    return ",".join(tokens)


def deserialize_bfs(data: str) -> BinaryNode | None:
    """Read the exact level-order encoding emitted by serialize_bfs."""
    tokens = iter(data.split(","))
    first = next(tokens)
    if first == "#":
        if next(tokens, None) is not None:
            raise ValueError("trailing tokens")
        return None
    root = BinaryNode(int(first))
    pending = deque([root])
    while pending:
        node = pending.popleft()
        children = []
        for _ in range(2):
            token = next(tokens, None)
            if token is None:
                raise ValueError("missing child token")
            child = None if token == "#" else BinaryNode(int(token))
            if child is not None:
                pending.append(child)
            children.append(child)
        node.left, node.right = children
    if next(tokens, None) is not None:
        raise ValueError("trailing tokens")
    return root
