# Implementation progress

- [x] Phase 1 · Topic structure, uv dependencies, Ruff, pytest, GitHub Actions
- [x] Phase 2 · Three graph representations and nine traversal lessons
- [x] Phase 3 · Graph connectivity, cycle detection, coloring, and topological sorting
- [x] Phase 4 · Shortest paths, disjoint sets, and minimum spanning trees
- [x] Phase 5 · SCCs, bridges, articulation points, special paths, DAG DP, flow, and matching
- [x] Phase 6 · Binary tree fundamentals, traversals, views, and properties
- [x] Phase 7 · Tree paths, relationships, construction, transformation, and serialization
- [x] Phase 8 · BST, balanced trees, heaps, and tries
- [x] Phase 9 · Segment trees, Fenwick trees, tree DP, and tree queries
- [x] Phase 10 · Multiway trees and advanced tree algorithms
- [x] Phase 11 · Reference guides, complete index, and interview checklist
- [x] Phase 12 · Full verification on the completed project
- [x] Phase 13 · Acceptance audit and GitHub push

## Verification

| Local Python | Dependency sync | Ruff lint | Ruff format check | pytest |
| --- | --- | --- | --- | --- |
| 3.10.22 | Passed | Passed | Passed | 301 passed |
| 3.12.16 | Passed | Passed | Passed | 301 passed |
| 3.14.6 | Passed | Passed | Passed | 301 passed |

The verification includes cross-checks against brute-force or independent
implementations for small inputs. Mixed-operation tests check ordering,
heights, black counts, occupancy, equal leaf depth, and B+ leaf links.

## Acceptance audit

- 73 graph lessons across all 15 graph topics and 132 tree lessons across all 19 tree topics.
- All 205 lesson directories have an implementation, a pytest file, and the 16 required README sections.
- Every lesson is linked from its topic and the root index. All relative Markdown links resolve locally.
- 254 Markdown files include the ten reference guides and the root and topic roadmaps.
- All 34 command-line examples ran successfully. Automatic tests also cover all lessons.
- Recursive implementations use Python's call stack. Lesson READMEs flag algorithms whose depth can make iterative variants preferable.
- Practice sections link to verified problems where included and provide clearly labeled original exercises throughout.

## GitHub

The [GitHub repository](https://github.com/ParthTagalpallewar/non-linear-dsa)
is public and uses `main` as its default branch. The GitHub Actions matrix
runs on pushes and pull requests for Python 3.10 and 3.14.
