"""Find Ultimate Parent."""


def find_ultimate_parent(parent: list[int], vertex: int) -> int:
    """Find a root in a valid parent forest without modifying links."""
    if not 0 <= vertex < len(parent):
        raise IndexError("vertex outside the forest")
    root = vertex
    while parent[root] != root:
        root = parent[root]

    return root
