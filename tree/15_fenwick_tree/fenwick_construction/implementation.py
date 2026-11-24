"""Binary Indexed Tree Construction."""

from tree.range_structures import FenwickTree


def fenwick_construction(values: list[int]) -> FenwickTree:
    """Build a Fenwick index in linear time."""
    return FenwickTree(values)


if __name__ == "__main__":
    print(fenwick_construction([3, 1, 4, 2, 8]).prefix_sum(4))
