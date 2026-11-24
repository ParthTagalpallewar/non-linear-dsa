"""Reusable nodes with identity semantics for relationship algorithms."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(eq=False)
class BinaryNode:
    """A binary-tree node with an integer value and up to two children."""

    value: int
    left: BinaryNode | None = None
    right: BinaryNode | None = None


@dataclass(eq=False)
class NaryNode:
    """An ordered N-ary tree node with an independent child list."""

    value: int
    children: list[NaryNode] = field(default_factory=list)
