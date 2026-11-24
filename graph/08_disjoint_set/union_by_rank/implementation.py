"""Union by Rank."""

from graph.disjoint_set import DisjointSet


class RankDisjointSet(DisjointSet):
    """Attach the lower-rank root beneath the higher-rank root."""

    def __init__(self, size: int) -> None:
        super().__init__(size)
        self.rank = [0] * size

    def union(self, first: int, second: int) -> bool:
        """Merge by rank and increase rank on an equal-rank merge."""
        left, right = self.find(first), self.find(second)
        if left == right:
            return False
        if self.rank[left] < self.rank[right]:
            left, right = right, left
        self.parent[right] = left
        self.size[left] += self.size[right]
        if self.rank[left] == self.rank[right]:
            self.rank[left] += 1
        return True
