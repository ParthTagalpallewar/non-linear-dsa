# Implementation progress

- [x] Phase 1 · Topic structure, uv dependencies, Ruff, pytest, GitHub Actions
- [x] Phase 2 · Three graph representations and nine traversal lessons
- [ ] Phase 3 · Graph connectivity, cycle detection, coloring, and topological sorting
- [ ] Phase 4 · Shortest paths, disjoint sets, and minimum spanning trees
- [ ] Phase 5 · SCCs, bridges, articulation points, special paths, DAG DP, flow, and matching
- [ ] Phase 6 · Binary tree fundamentals, traversals, views, and properties
- [ ] Phase 7 · Tree paths, relationships, construction, transformation, and serialization
- [ ] Phase 8 · BST, balanced trees, heaps, and tries
- [ ] Phase 9 · Segment trees, Fenwick trees, tree DP, and tree queries
- [ ] Phase 10 · Multiway trees and advanced tree algorithms
- [ ] Phase 11 · Reference guides, complete index, and interview checklist
- [ ] Phase 12 · Full verification on the completed project
- [ ] Phase 13 · Acceptance audit and GitHub push

## Verification

The first 12 lessons have a 16-section README, implementation, and tests.
On Python 3.12, locked dependency sync, Ruff linting and formatting checks,
and pytest passed with 25 tests. Relative Markdown links resolved locally.
The CI workflow covers Python 3.10 and 3.14 and awaits a GitHub run.

## Next task

Start phase 3 in `graph/03_connectivity` with connected components using BFS,
DFS, and DSU in separate lesson directories. Implement basic DSU in
`graph/08_disjoint_set` as a dependency and reuse it for DSU cycle detection.
Then implement all six cycle-detection and safe-node lessons, three coloring
lessons, and four topological-sort, dependency, and scheduling lessons.
Run the checks and commit once phase 3 is verified. Use the original request
for the full pending algorithm inventory and the established lesson READMEs
for the documentation format.

## GitHub

The connector authenticated as `ParthTagalpallewar` and returned HTTP 404 for
`ParthTagalpallewar/non-linear-dsa`. Its available tools lack repository
creation. GitHub CLI is absent and local HTTPS credential lookup returned no
credential. Local work is committed on `main`. Creating the private repository
and pushing the commits requires an authenticated GitHub creation and push path.
