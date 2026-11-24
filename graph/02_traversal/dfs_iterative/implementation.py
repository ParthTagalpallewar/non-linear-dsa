"""Iterative Depth-First Search."""


def dfs_iterative(graph: dict[int, list[int]], start: int) -> list[int]:
    """Return recursive-style preorder using explicit neighbor iterators."""
    visited = {start}
    order = [start]
    stack = [iter(graph.get(start, []))]
    while stack:
        neighbor = next(stack[-1], None)
        if neighbor is None:
            stack.pop()
        elif neighbor not in visited:
            visited.add(neighbor)
            order.append(neighbor)
            stack.append(iter(graph.get(neighbor, [])))
    return order
