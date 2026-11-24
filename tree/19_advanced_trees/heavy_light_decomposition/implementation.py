"""Heavy-Light Decomposition."""

from tree.range_structures import FenwickTree
from tree.rooted import root_tree, subtree_sizes


class HeavyLight:
    """Maintain vertex path sums under point assignments."""

    def __init__(self, graph: list[list[int]], values: list[int], root: int = 0):
        if len(graph) != len(values):
            raise ValueError("provide one value per vertex")
        tree = root_tree(graph, root)
        self.parent = tree.parent
        self.depth = tree.depth
        self.head = [-1] * len(graph)
        self.position = [-1] * len(graph)
        sizes = subtree_sizes(tree)
        ordered_values = []
        pending = [(root, root)] if tree.order else []
        while pending:
            vertex, head = pending.pop()
            self.head[vertex] = head
            self.position[vertex] = len(ordered_values)
            ordered_values.append(values[vertex])
            children = [
                child for child in graph[vertex] if tree.parent[child] == vertex
            ]
            if children:
                heavy = max(children, key=sizes.__getitem__)
                pending.extend((child, child) for child in children if child != heavy)
                pending.append((heavy, head))
        self._sums = FenwickTree(ordered_values)
        self._values = values.copy()

    def _check(self, vertex: int) -> None:
        if not 0 <= vertex < len(self.parent):
            raise IndexError("vertex outside the tree")

    def point_set(self, vertex: int, value: int) -> None:
        """Replace one vertex value."""
        self._check(vertex)
        self._sums.add(self.position[vertex], value - self._values[vertex])
        self._values[vertex] = value

    def path_sum(self, left: int, right: int) -> int:
        """Return the inclusive sum along the path between the vertices."""
        self._check(left)
        self._check(right)
        total = 0
        while self.head[left] != self.head[right]:
            if self.depth[self.head[left]] < self.depth[self.head[right]]:
                left, right = right, left
            head = self.head[left]
            total += self._sums.range_sum(self.position[head], self.position[left] + 1)
            left = self.parent[head]
        start, stop = sorted((self.position[left], self.position[right]))
        return total + self._sums.range_sum(start, stop + 1)


def heavy_light_decomposition(
    graph: list[list[int]], values: list[int], root: int = 0
) -> HeavyLight:
    """Index a static tree for dynamic point updates and path queries."""
    return HeavyLight(graph, values, root)
