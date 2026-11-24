"""Hopcroft–Karp Algorithm."""

from collections import deque


def hopcroft_karp(graph: list[list[int]], right_size: int) -> list[tuple[int, int]]:
    """Return a maximum bipartite matching using shortest augmenting layers."""
    left_size = len(graph)
    partner_left = [-1] * left_size
    partner_right = [-1] * right_size
    unreachable = left_size + 1
    while True:
        distance = [unreachable] * left_size
        queue = deque()
        for left, right in enumerate(partner_left):
            if right == -1:
                distance[left] = 0
                queue.append(left)
        shortest = unreachable
        while queue:
            left = queue.popleft()
            if distance[left] >= shortest:
                continue
            for right in graph[left]:
                other = partner_right[right]
                if other == -1:
                    shortest = distance[left] + 1
                elif distance[other] == unreachable:
                    distance[other] = distance[left] + 1
                    queue.append(other)
        if shortest == unreachable:
            return [
                (left, right) for left, right in enumerate(partner_left) if right >= 0
            ]

        next_edge = [0] * left_size

        def assign(left: int) -> bool:
            while next_edge[left] < len(graph[left]):
                right = graph[left][next_edge[left]]
                next_edge[left] += 1
                other = partner_right[right]
                following = distance[left] + 1
                if other == -1:
                    if following != shortest:
                        continue
                elif (
                    following >= shortest
                    or distance[other] != following
                    or not assign(other)
                ):
                    continue
                partner_left[left] = right
                partner_right[right] = left
                return True
            distance[left] = unreachable
            return False

        for left, right in enumerate(partner_left):
            if right == -1:
                assign(left)
