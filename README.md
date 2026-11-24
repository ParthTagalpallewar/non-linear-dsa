# Non-Linear DSA

Learn to recognize, implement, and explain graph and tree algorithms in Python for software engineering interviews.

Start with representations and traversals, then move to connectivity, paths, and ordering. For trees, work through binary traversals and search trees before range queries and specialized structures.

- [ ] [Graph roadmap](graph/README.md)
- [ ] [Tree roadmap](tree/README.md)

Use P1 for interview essentials, P2 for advanced interview topics, and P3 for specialized or competitive-programming techniques.

## Installation and checks

Requires Python 3.10 or later and uv. Run these commands from the repository root.

```sh
uv sync
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

To format source files, run `uv run ruff format .`. Each lesson links to its implementation and tests.

See [project progress](PROGRESS.md) for the current coverage and next task.
