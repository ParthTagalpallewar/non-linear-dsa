"""Preprocessed static tree queries using ancestor powers and Euler tours."""

from tree.rooted import root_tree


class BinaryLifting:
    """Index ancestors at distances that are powers of two."""

    def __init__(self, graph: list[list[int]], root: int = 0) -> None:
        tree = root_tree(graph, root)
        self.depth = tree.depth
        self.up = [tree.parent]
        for _ in range(1, len(graph).bit_length()):
            previous = self.up[-1]
            self.up.append([previous[p] if p != -1 else -1 for p in previous])

    def _validate(self, vertex: int) -> None:
        if not 0 <= vertex < len(self.depth):
            raise IndexError("vertex outside the tree")

    def kth_ancestor(self, vertex: int, steps: int) -> int | None:
        """Jump upward exactly steps edges, if such an ancestor exists."""
        self._validate(vertex)
        if steps < 0:
            raise ValueError("steps must be nonnegative")
        if steps > self.depth[vertex]:
            return None
        while steps:
            bit = steps & -steps
            vertex = self.up[bit.bit_length() - 1][vertex]
            steps ^= bit
        return vertex

    def lca(self, left: int, right: int) -> int:
        """Return the deepest common ancestor."""
        self._validate(left)
        self._validate(right)
        if self.depth[left] < self.depth[right]:
            left, right = right, left
        aligned = self.kth_ancestor(left, self.depth[left] - self.depth[right])
        assert aligned is not None
        left = aligned
        if left == right:
            return left
        for column in reversed(self.up):
            if column[left] != column[right]:
                left, right = column[left], column[right]
        return self.up[0][left]


def euler_walk(graph: list[list[int]], root: int = 0) -> tuple[list[int], list[int]]:
    """Record each tree-edge traversal and the first position of each vertex."""
    tree = root_tree(graph, root)
    if not tree.order:
        return [], []
    walk = []
    first = [-1] * len(graph)
    pending = [(root, True)]
    while pending:
        vertex, entering = pending.pop()
        if entering:
            first[vertex] = len(walk)
            for child in reversed(graph[vertex]):
                if tree.parent[child] == vertex:
                    pending.append((vertex, False))
                    pending.append((child, True))
        walk.append(vertex)
    return walk, first


class EulerLCA:
    """Use a sparse table for constant-time LCA after Euler preprocessing."""

    def __init__(self, graph: list[list[int]], root: int = 0) -> None:
        walk, self.first = euler_walk(graph, root)
        self.depth = root_tree(graph, root).depth
        self.table = [walk]
        length = 2
        while length <= len(walk):
            earlier = self.table[-1]
            half = length // 2
            self.table.append(
                [
                    self._shallower(earlier[i], earlier[i + half])
                    for i in range(len(walk) - length + 1)
                ]
            )
            length *= 2

    def _shallower(self, left: int, right: int) -> int:
        return left if self.depth[left] <= self.depth[right] else right

    def lca(self, left: int, right: int) -> int:
        """Find the shallowest Euler vertex between the first visits."""
        if not (0 <= left < len(self.first) and 0 <= right < len(self.first)):
            raise IndexError("vertex outside the tree")
        start, end = sorted((self.first[left], self.first[right]))
        level = (end - start + 1).bit_length() - 1
        width = 1 << level
        return self._shallower(
            self.table[level][start], self.table[level][end - width + 1]
        )
