"""Flood Fill."""

from graph.grid import Cell, neighbors


def flood_fill(image: list[list[int]], start: Cell, color: int) -> list[list[int]]:
    """Recolor a four-connected region in place in a rectangular image."""
    rows, columns = len(image), len(image[0]) if image else 0
    row, column = start
    if not (0 <= row < rows and 0 <= column < columns):
        raise ValueError("start must be inside the image")
    original = image[row][column]
    if original == color:
        return image
    image[row][column] = color
    stack = [start]
    while stack:
        for nr, nc in neighbors(stack.pop(), rows, columns):
            if image[nr][nc] == original:
                image[nr][nc] = color
                stack.append((nr, nc))
    return image
