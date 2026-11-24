"""Array-backed binary heaps with an explicit ordering direction."""

from collections.abc import Iterable


def preferred(left: int, right: int, reverse: bool) -> bool:
    """Whether left belongs above right in the selected heap order."""
    return left > right if reverse else left < right


def sift_down(data: list[int], index: int, stop: int, reverse: bool) -> None:
    """Restore one parent in the heap prefix [0, stop)."""
    while 2 * index + 1 < stop:
        child = 2 * index + 1
        right = child + 1
        if right < stop and preferred(data[right], data[child], reverse):
            child = right
        if not preferred(data[child], data[index], reverse):
            return
        data[index], data[child] = data[child], data[index]
        index = child


class BinaryHeap:
    """A min-heap by default, or a max-heap when reverse is true."""

    def __init__(self, values: Iterable[int] = (), *, reverse: bool = False) -> None:
        self.data = list(values)
        self.reverse = reverse
        for index in range(len(self.data) // 2 - 1, -1, -1):
            sift_down(self.data, index, len(self.data), self.reverse)

    def __len__(self) -> int:
        return len(self.data)

    def push(self, value: int) -> None:
        """Append and move the new value above any lower-priority parents."""
        self.data.append(value)
        index = len(self.data) - 1
        while index:
            parent = (index - 1) // 2
            if not preferred(self.data[index], self.data[parent], self.reverse):
                break
            self.data[parent], self.data[index] = self.data[index], self.data[parent]
            index = parent

    def peek(self) -> int:
        """Return the highest-priority value without removing it."""
        return self.data[0]

    def pop(self) -> int:
        """Remove the root and repair the heap with the last item."""
        result = self.peek()
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            sift_down(self.data, 0, len(self.data), self.reverse)
        return result
