"""Tarjan’s SCC Algorithm."""


def tarjan_scc(graph: list[list[int]]) -> list[list[int]]:
    """Return SCCs in reverse topological order of the component DAG."""
    entry = [-1] * len(graph)
    low = [0] * len(graph)
    active = [False] * len(graph)
    stack: list[int] = []
    groups: list[list[int]] = []
    clock = 0

    def visit(vertex: int) -> None:
        nonlocal clock
        entry[vertex] = low[vertex] = clock
        clock += 1
        stack.append(vertex)
        active[vertex] = True
        for target in graph[vertex]:
            if entry[target] == -1:
                visit(target)
                low[vertex] = min(low[vertex], low[target])
            elif active[target]:
                low[vertex] = min(low[vertex], entry[target])
        if low[vertex] == entry[vertex]:
            group = []
            while True:
                member = stack.pop()
                active[member] = False
                group.append(member)
                if member == vertex:
                    break
            groups.append(group)

    for vertex in range(len(graph)):
        if entry[vertex] == -1:
            visit(vertex)
    return groups
