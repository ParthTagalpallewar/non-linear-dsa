"""Half-open range query structures with zero-based public indices."""

from typing import Literal

Aggregate = Literal["sum", "min", "max"]


class SegmentTree:
    """Maintain sum, minimum, or maximum with lazy range addition."""

    def __init__(self, values: list[int], aggregate: Aggregate = "sum") -> None:
        if aggregate not in ("sum", "min", "max"):
            raise ValueError("unknown aggregate")
        self.size = len(values)
        self.aggregate = aggregate
        self.data = [0] * (4 * self.size)
        self.lazy = [0] * (4 * self.size)
        if values:
            self._build(values, 1, 0, self.size)

    def _combine(self, left: int, right: int) -> int:
        if self.aggregate == "sum":
            return left + right
        return min(left, right) if self.aggregate == "min" else max(left, right)

    def _build(self, values: list[int], node: int, start: int, end: int) -> None:
        if end - start == 1:
            self.data[node] = values[start]
            return
        middle = (start + end) // 2
        self._build(values, 2 * node, start, middle)
        self._build(values, 2 * node + 1, middle, end)
        self.data[node] = self._combine(self.data[2 * node], self.data[2 * node + 1])

    def _apply(self, node: int, size: int, delta: int) -> None:
        self.data[node] += delta * size if self.aggregate == "sum" else delta
        self.lazy[node] += delta

    def _push(self, node: int, start: int, middle: int, end: int) -> None:
        if delta := self.lazy[node]:
            self._apply(2 * node, middle - start, delta)
            self._apply(2 * node + 1, end - middle, delta)
            self.lazy[node] = 0

    def _check(self, left: int, right: int) -> None:
        if not 0 <= left <= right <= self.size:
            raise IndexError("invalid half-open range")

    def range_add(self, left: int, right: int, delta: int) -> None:
        """Add delta to each element in [left, right)."""
        self._check(left, right)
        if left == right:
            return

        def update(node: int, start: int, end: int) -> None:
            if left <= start and end <= right:
                self._apply(node, end - start, delta)
                return
            middle = (start + end) // 2
            self._push(node, start, middle, end)
            if left < middle:
                update(2 * node, start, middle)
            if middle < right:
                update(2 * node + 1, middle, end)
            self.data[node] = self._combine(
                self.data[2 * node], self.data[2 * node + 1]
            )

        update(1, 0, self.size)

    def query(self, left: int, right: int) -> int:
        """Return the aggregate of a nonempty interval, or zero for empty sums."""
        self._check(left, right)
        if left == right:
            if self.aggregate == "sum":
                return 0
            raise ValueError("min/max of an empty range")

        def inspect(node: int, start: int, end: int) -> int:
            if left <= start and end <= right:
                return self.data[node]
            middle = (start + end) // 2
            self._push(node, start, middle, end)
            if right <= middle:
                return inspect(2 * node, start, middle)
            if middle <= left:
                return inspect(2 * node + 1, middle, end)
            return self._combine(
                inspect(2 * node, start, middle), inspect(2 * node + 1, middle, end)
            )

        return inspect(1, 0, self.size)

    def point_set(self, index: int, value: int) -> None:
        """Replace the value at an index."""
        current = self.query(index, index + 1)
        self.range_add(index, index + 1, value - current)


class FenwickTree:
    """Maintain point additions, prefix sums, and range sums."""

    def __init__(self, values: list[int]) -> None:
        self.size = len(values)
        self.data = [0, *values]
        for index in range(1, self.size + 1):
            parent = index + (index & -index)
            if parent <= self.size:
                self.data[parent] += self.data[index]

    def add(self, index: int, delta: int) -> None:
        """Add delta at a zero-based index."""
        if not 0 <= index < self.size:
            raise IndexError("invalid index")
        index += 1
        while index <= self.size:
            self.data[index] += delta
            index += index & -index

    def prefix_sum(self, end: int) -> int:
        """Return the sum over [0, end)."""
        if not 0 <= end <= self.size:
            raise IndexError("invalid prefix")
        result = 0
        while end:
            result += self.data[end]
            end -= end & -end
        return result

    def range_sum(self, left: int, right: int) -> int:
        """Return the sum over [left, right)."""
        if left > right:
            raise IndexError("invalid half-open range")
        return self.prefix_sum(right) - self.prefix_sum(left)


class RangeFenwick:
    """Maintain range additions and range sums with two Fenwick trees."""

    def __init__(self, values: list[int]) -> None:
        self.size = len(values)
        previous = 0
        differences = []
        for value in values:
            differences.append(value - previous)
            previous = value
        self._diff = FenwickTree(differences)
        self._weighted = FenwickTree(
            [index * delta for index, delta in enumerate(differences)]
        )

    def range_add(self, left: int, right: int, delta: int) -> None:
        """Add delta to every index in [left, right)."""
        if not 0 <= left <= right <= self.size:
            raise IndexError("invalid half-open range")
        if left < right:
            self._diff.add(left, delta)
            self._weighted.add(left, left * delta)
            if right < self.size:
                self._diff.add(right, -delta)
                self._weighted.add(right, -right * delta)

    def prefix_sum(self, end: int) -> int:
        """Compute the sum of reconstructed values before end."""
        return end * self._diff.prefix_sum(end) - self._weighted.prefix_sum(end)

    def range_sum(self, left: int, right: int) -> int:
        """Return the sum over [left, right)."""
        if left > right:
            raise IndexError("invalid half-open range")
        return self.prefix_sum(right) - self.prefix_sum(left)
