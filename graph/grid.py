"""Four-directional neighbors shared by grid lessons."""

from collections.abc import Iterator

Cell = tuple[int, int]


def neighbors(cell: Cell, rows: int, columns: int) -> Iterator[Cell]:
    """Yield in-bounds neighbors in down, up, right, left order."""
    row, column = cell
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = row + dr, column + dc
        if 0 <= nr < rows and 0 <= nc < columns:
            yield nr, nc
