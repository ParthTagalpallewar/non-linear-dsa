"""Bipartite Matching Using Augmenting Paths."""


def bipartite_matching(
    graph: list[list[int]], right_size: int
) -> list[tuple[int, int]]:
    """Return maximum-cardinality pairs (left, right), sorted by left ID."""
    matched = [-1] * right_size

    def assign(left: int, seen: set[int]) -> bool:
        for right in graph[left]:
            if right in seen:
                continue
            seen.add(right)
            if matched[right] == -1 or assign(matched[right], seen):
                matched[right] = left
                return True
        return False

    for left in range(len(graph)):
        assign(left, set())
    return sorted((left, right) for right, left in enumerate(matched) if left != -1)
