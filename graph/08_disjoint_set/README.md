# Disjoint Sets

A disjoint-set union (DSU) stores a partition of elements. Each set is
represented by a rooted parent tree. Find returns the root and union joins
two distinct roots. Union by size tracks exact component cardinality.
Union by rank tracks an upper bound on tree height and increases the rank
only when two equal-rank roots merge. Path compression can reduce actual
height without changing ranks. Either heuristic combined with compression
gives amortized O(α(V)) per operation for V elements after O(V) setup.
The inverse Ackermann function α grows extremely slowly.

## Lessons

- [ ] [Basic Disjoint Set](basic_disjoint_set/README.md) · P1
- [ ] [Find Ultimate Parent](find_ultimate_parent/README.md) · P1
- [ ] [Path Compression](compress_path/README.md) · P1
- [ ] [Union by Rank](union_by_rank/README.md) · P1
- [ ] [Union by Size](union_by_size/README.md) · P1
- [ ] [Dynamic Connectivity with Insertions](dynamic_connectivity/README.md) · P1
- [ ] [Lexicographically Smallest Equivalent String](smallest_equivalent_string/README.md) · P1
