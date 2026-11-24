"""Bidirectional BFS."""


def bidirectional_bfs(
    graph: dict[int, list[int]], start: int, target: int
) -> int | None:
    """Find the fewest edges in an undirected graph with symmetric adjacency."""
    if start == target:
        return 0
    frontier, other_frontier = {start}, {target}
    distances, other_distances = {start: 0}, {target: 0}
    while frontier and other_frontier:
        if len(frontier) > len(other_frontier):
            frontier, other_frontier = other_frontier, frontier
            distances, other_distances = other_distances, distances
        next_frontier = set()
        for vertex in frontier:
            for neighbor in graph.get(vertex, []):
                if neighbor in other_distances:
                    return distances[vertex] + 1 + other_distances[neighbor]
                if neighbor not in distances:
                    distances[neighbor] = distances[vertex] + 1
                    next_frontier.add(neighbor)
        frontier = next_frontier
    return None
