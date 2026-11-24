# Network Flow

A flow routes supply from a source to a sink within edge capacities, conserving flow at internal vertices. Residual edges represent available increases and reverse edges allow previous flow to be cancelled. An augmenting path sends additional flow equal to the smallest residual capacity along the path. When no such path remains, the vertices reachable from the source define a cut with capacity equal to the flow. This is the max-flow min-cut theorem.

## Lessons

- [ ] [Ford–Fulkerson](ford_fulkerson/README.md) · P2
- [ ] [Edmonds–Karp](edmonds_karp/README.md) · P2
- [ ] [Maximum Flow](maximum_flow/README.md) · P2
- [ ] [Dinic’s Algorithm](dinic/README.md) · P3
- [ ] [Minimum Source–Sink Cut](minimum_cut/README.md) · P2
