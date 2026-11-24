"""LCA Using Euler Tour and Sparse Table."""

from tree.queries import EulerLCA


def lca_euler_sparse_table(index: EulerLCA, left: int, right: int) -> int:
    """Answer a lowest-common-ancestor query via an Euler depth minimum."""
    return index.lca(left, right)
