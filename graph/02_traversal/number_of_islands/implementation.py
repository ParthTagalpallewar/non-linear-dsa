"""Number of Islands."""

from graph.grid import Cell, neighbors


def number_of_islands(grid: list[list[int]]) -> int:
    """Count four-connected groups of ones in a rectangular binary grid."""
    rows, columns = len(grid), len(grid[0]) if grid else 0
    visited: set[Cell] = set()
    count = 0
    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 0 or (row, column) in visited:
                continue
            count += 1
            visited.add((row, column))
            stack = [(row, column)]
            while stack:
                for nr, nc in neighbors(stack.pop(), rows, columns):
                    if grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        stack.append((nr, nc))
    return count
