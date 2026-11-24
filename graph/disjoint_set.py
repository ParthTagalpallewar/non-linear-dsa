"""Disjoint sets with path halving and union by size."""


class DisjointSet:
    """Maintain disjoint groups of integers from zero through size - 1."""

    def __init__(self, size: int) -> None:
        if size < 0:
            raise ValueError("size must be nonnegative")
        self.parent = list(range(size))
        self.size = [1] * size

    def find(self, vertex: int) -> int:
        """Return the representative, shortening paths along the way."""
        if not 0 <= vertex < len(self.parent):
            raise IndexError("vertex outside the disjoint set")
        while vertex != self.parent[vertex]:
            self.parent[vertex] = self.parent[self.parent[vertex]]
            vertex = self.parent[vertex]
        return vertex

    def union(self, first: int, second: int) -> bool:
        """Merge two groups and report whether their representatives differed."""
        left, right = self.find(first), self.find(second)
        if left == right:
            return False
        if self.size[left] < self.size[right]:
            left, right = right, left
        self.parent[right] = left
        self.size[left] += self.size[right]
        return True
