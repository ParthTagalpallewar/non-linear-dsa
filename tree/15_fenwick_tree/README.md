# Fenwick Trees

The lowest set bit of i is i & −i. In two's-complement arithmetic, negating i inverts its trailing bits and adds one, leaving a single shared low bit. The one-indexed entry i stores the i & −i elements ending there. Subtracting that bit walks disjoint blocks in a prefix. Adding it visits every larger block containing an updated position. Both walks change O(log N) bits. See the [complete Fenwick implementations](../range_structures.py).

## Lessons

- [ ] [Binary Indexed Tree Construction](fenwick_construction/README.md) · P2
- [ ] [Fenwick Prefix Sum Query](fenwick_prefix_sum/README.md) · P2
- [ ] [Fenwick Range Sum Query](fenwick_range_sum/README.md) · P2
- [ ] [Fenwick Point Update](fenwick_point_update/README.md) · P2
- [ ] [Fenwick Range Update](fenwick_range_update/README.md) · P2
