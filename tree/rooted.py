"""Root a numbered undirected simple tree and index its preorder."""

from dataclasses import dataclass


@dataclass
class RootedTree:
    """Parent, depth, preorder vertices, and half-open subtree intervals."""

    parent: list[int]
    depth: list[int]
    order: list[int]
    start: list[int]
    end: list[int]


def root_tree(graph: list[list[int]], root: int = 0) -> RootedTree:
    """Index an undirected, symmetric adjacency list, rooted at root."""
    size = len(graph)
    if not size:
        return RootedTree([], [], [], [], [])
    if not 0 <= root < size:
        raise IndexError("root outside the tree")
    if sum(map(len, graph)) != 2 * (size - 1):
        raise ValueError("expected an undirected tree")
    parent = [-2] * size
    parent[root] = -1
    depth = [0] * size
    start = [0] * size
    end = [0] * size
    order: list[int] = []
    stack = [(root, False)]
    while stack:
        vertex, exiting = stack.pop()
        if exiting:
            end[vertex] = len(order)
            continue
        start[vertex] = len(order)
        order.append(vertex)
        stack.append((vertex, True))
        for target in reversed(graph[vertex]):
            if not 0 <= target < size:
                raise IndexError("target outside the tree")
            if target == parent[vertex]:
                continue
            if parent[target] != -2:
                raise ValueError("cycle in tree")
            parent[target] = vertex
            depth[target] = depth[vertex] + 1
            stack.append((target, False))
    if len(order) != size:
        raise ValueError("disconnected tree")
    return RootedTree(parent, depth, order, start, end)


def subtree_sizes(tree: RootedTree) -> list[int]:
    """Use preorder intervals to count descendants including each root."""
    return [end - start for start, end in zip(tree.start, tree.end, strict=True)]
