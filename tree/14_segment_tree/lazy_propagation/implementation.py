"""Lazy Propagation."""

from tree.range_structures import SegmentTree


def lazy_propagation(
    values: list[int], updates: list[tuple[int, int, int]]
) -> list[int]:
    """Apply deferred range additions and report the full sum after each update."""
    tree = SegmentTree(values)
    sums = []
    for left, right, delta in updates:
        tree.range_add(left, right, delta)
        sums.append(tree.query(0, len(values)))
    return sums


if __name__ == "__main__":
    print(lazy_propagation([1, 2, 3, 4], [(0, 4, 2), (1, 3, -1)]))
