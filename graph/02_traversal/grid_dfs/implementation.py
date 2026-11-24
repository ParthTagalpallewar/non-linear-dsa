"""Grid DFS."""

from graph.grid import Cell, neighbors


def grid_dfs(grid: list[list[int]], start: Cell) -> list[Cell]:
    """Visit reachable cells in a rectangular grid where zero means passable."""
    rows, columns = len(grid), len(grid[0]) if grid else 0
    row, column = start
    if not (0 <= row < rows and 0 <= column < columns and grid[row][column] == 0):
        return []
    visited = {start}
    pending = [start]
    order = []
    while pending:
        cell = pending.pop()
        order.append(cell)
        for nr, nc in neighbors(cell, rows, columns):
            if grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                pending.append((nr, nc))
    return order
