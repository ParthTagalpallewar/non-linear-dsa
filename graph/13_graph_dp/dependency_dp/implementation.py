"""Dependency-Based Dynamic Programming."""

from graph.topological import kahn_order


def dependency_dp(prerequisites: list[list[int]], base_costs: list[int]) -> list[int]:
    """Compute additive costs, charging again for each dependency occurrence."""
    if len(prerequisites) != len(base_costs):
        raise ValueError("provide one base cost per task")
    dependents: list[list[int]] = [[] for _ in prerequisites]
    for task, needs in enumerate(prerequisites):
        for need in needs:
            dependents[need].append(task)
    order = kahn_order(dependents)
    if len(order) != len(prerequisites):
        raise ValueError("dependencies contain a cycle")
    totals = base_costs.copy()
    for task in order:
        for dependent in dependents[task]:
            totals[dependent] += totals[task]
    return totals
