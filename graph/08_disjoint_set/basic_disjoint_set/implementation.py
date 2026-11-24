"""Basic Disjoint Set."""


class BasicDisjointSet:
    """Maintain disjoint sets over 0 through size−1 without heuristics."""

    def __init__(self, size: int) -> None:
        if size < 0:
            raise ValueError("size must be nonnegative")
        self.parent = list(range(size))

    def find(self, vertex: int) -> int:
        """Follow parent links to the root."""
        if not 0 <= vertex < len(self.parent):
            raise IndexError("vertex outside the disjoint set")
        while self.parent[vertex] != vertex:
            vertex = self.parent[vertex]
        return vertex

    def union(self, first: int, second: int) -> bool:
        """Attach one root to the other and report whether they differed."""
        first, second = self.find(first), self.find(second)
        if first == second:
            return False
        self.parent[second] = first
        return True
