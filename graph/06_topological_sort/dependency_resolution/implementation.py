"""Dependency Resolution."""

from collections.abc import Iterable, Mapping

from graph.topological import kahn_order


def dependency_resolution(dependencies: Mapping[str, Iterable[str]]) -> list[str]:
    """Order named tasks given a mapping from each task to its requirements."""
    ids: dict[str, int] = {}
    graph: list[list[int]] = []

    def get_id(task: str) -> int:
        if task not in ids:
            ids[task] = len(graph)
            graph.append([])
        return ids[task]

    for task, requirements in dependencies.items():
        target = get_id(task)
        for requirement in requirements:
            source = get_id(requirement)
            graph[source].append(target)
    order = kahn_order(graph)
    if len(order) != len(graph):
        raise ValueError("dependencies contain a cycle")
    names = list(ids)
    return [names[vertex] for vertex in order]
