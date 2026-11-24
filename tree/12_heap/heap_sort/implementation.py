"""Heap Sort."""

from tree.heaps import sift_down


def heap_sort(values: list[int]) -> None:
    """Sort values ascending in place using a max heap."""
    for index in range(len(values) // 2 - 1, -1, -1):
        sift_down(values, index, len(values), True)
    for end in range(len(values) - 1, 0, -1):
        values[0], values[end] = values[end], values[0]
        sift_down(values, 0, end, True)


if __name__ == "__main__":
    values = [4, 1, 3]
    heap_sort(values)
    print(values)
