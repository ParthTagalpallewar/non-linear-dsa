"""Hungarian Assignment Algorithm."""

from math import inf


def hungarian(cost: list[list[int]]) -> tuple[int, list[int]]:
    """Assign each row to a distinct column, minimizing integer cost."""
    rows = len(cost)
    if not rows:
        return 0, []
    columns = len(cost[0])
    if columns < rows or any(len(row) != columns for row in cost):
        raise ValueError("require a rectangular matrix with at least as many columns")
    row_potential = [0] * (rows + 1)
    column_potential = [0] * (columns + 1)
    owner = [0] * (columns + 1)
    previous = [0] * (columns + 1)
    for row in range(1, rows + 1):
        owner[0] = row
        column = 0
        used = [False] * (columns + 1)
        slack = [inf] * (columns + 1)
        while True:
            used[column] = True
            current = owner[column]
            delta = inf
            next_column = 0
            for target in range(1, columns + 1):
                if used[target]:
                    continue
                reduced = (
                    cost[current - 1][target - 1]
                    - row_potential[current]
                    - column_potential[target]
                )
                if reduced < slack[target]:
                    slack[target] = reduced
                    previous[target] = column
                if slack[target] < delta:
                    delta = slack[target]
                    next_column = target
            for target in range(columns + 1):
                if used[target]:
                    row_potential[owner[target]] += int(delta)
                    column_potential[target] -= int(delta)
                else:
                    slack[target] -= delta
            column = next_column
            if owner[column] == 0:
                break
        while column:
            source = previous[column]
            owner[column] = owner[source]
            column = source
    assignment = [-1] * rows
    for column in range(1, columns + 1):
        if owner[column]:
            assignment[owner[column] - 1] = column - 1
    return sum(cost[row][column] for row, column in enumerate(assignment)), assignment


if __name__ == "__main__":
    print(hungarian([[4, 1], [3, 2]]))
