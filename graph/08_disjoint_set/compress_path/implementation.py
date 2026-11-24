"""Path Compression."""


def compress_path(parent: list[int], vertex: int) -> int:
    """Find the root and attach all traversed vertices directly to it."""
    if not 0 <= vertex < len(parent):
        raise IndexError("vertex outside the forest")
    root = vertex
    while parent[root] != root:
        root = parent[root]
    while vertex != root:
        previous = parent[vertex]
        parent[vertex] = root
        vertex = previous
    return root
