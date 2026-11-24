"""Dinic’s Algorithm."""

from collections import deque

from graph.flow import CapacityEdge, augment, residual_network


def dinic(size: int, edges: list[CapacityEdge], source: int, sink: int) -> int:
    """Compute maximum flow using BFS layers and blocking flows."""
    graph = residual_network(size, edges, source, sink)
    total = 0
    bound = sum(arc.capacity for arc in graph[source])
    while True:
        level = [-1] * size
        level[source] = 0
        queue = deque([source])
        while queue:
            vertex = queue.popleft()
            for arc in graph[vertex]:
                if arc.capacity and level[arc.target] == -1:
                    level[arc.target] = level[vertex] + 1
                    queue.append(arc.target)
        if level[sink] == -1:
            return total
        next_edge = [0] * size

        def send(vertex: int, amount: int) -> int:
            if vertex == sink:
                return amount
            while next_edge[vertex] < len(graph[vertex]):
                arc = graph[vertex][next_edge[vertex]]
                if arc.capacity and level[arc.target] == level[vertex] + 1:
                    sent = send(arc.target, min(amount, arc.capacity))
                    if sent:
                        augment(graph, vertex, arc, sent)
                        return sent
                next_edge[vertex] += 1
            return 0

        while sent := send(source, bound):
            total += sent
