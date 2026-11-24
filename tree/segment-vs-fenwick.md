# Segment tree vs Fenwick tree

| Requirement | Segment tree | Fenwick tree |
| --- | --- | --- |
| Point add with sum queries | Supported | Supported |
| Point assignment | Read and replace or apply a delta | Compute delta and add |
| Range min/max | Supported with the matching combine rule | A standard prefix-sum Fenwick cannot subtract minima/maxima |
| Range adds and range sums | Lazy propagation | Two Fenwick trees of weighted differences |
| Build | O(N) | O(N) |
| Query/update | O(log(N + 1)) | O(log(N + 1)) |
| Storage | O(N), with interval and lazy arrays | O(N), usually one or two compact arrays |

Fenwick prefix walks use the low bit to partition [0, end). Subtracting two
prefix sums gives an arbitrary interval sum. Segment trees decompose any
half-open interval directly into covered tree nodes. An associative combine
operation is enough for range queries. A corresponding update rule must
also specify how a tag changes an aggregate and how multiple tags compose.

Use [Fenwick](15_fenwick_tree/README.md) for sums when compactness matters.
Use a [segment tree](14_segment_tree/README.md) for richer summaries, lazy
updates, or queries that need more control over interval structure.
