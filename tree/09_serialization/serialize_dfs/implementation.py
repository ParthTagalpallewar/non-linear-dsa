"""Serialization and Deserialization Using DFS."""

from tree.nodes import BinaryNode


def serialize_dfs(root: BinaryNode | None) -> str:
    """Encode preorder values and explicit nulls, separated by commas."""
    tokens = []
    pending = [root]
    while pending:
        node = pending.pop()
        if node is None:
            tokens.append("#")
        else:
            tokens.append(str(node.value))
            pending.extend((node.right, node.left))
    return ",".join(tokens)


def deserialize_dfs(data: str) -> BinaryNode | None:
    """Read the exact preorder encoding emitted by serialize_dfs."""
    tokens = iter(data.split(","))

    def read() -> BinaryNode | None:
        token = next(tokens, None)
        if token is None:
            raise ValueError("missing child token")
        if token == "#":
            return None
        return BinaryNode(int(token), read(), read())

    root = read()
    if next(tokens, None) is not None:
        raise ValueError("trailing tokens")
    return root
