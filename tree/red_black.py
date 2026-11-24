"""Left-leaning red-black trees with top-down deletion."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RedBlackNode:
    """The color represents the incoming edge from the parent."""

    key: int
    red: bool = True
    left: RedBlackNode | None = None
    right: RedBlackNode | None = None


def red(node: RedBlackNode | None) -> bool:
    """Treat empty leaves as black."""
    return node is not None and node.red


def rotate_left(node: RedBlackNode) -> RedBlackNode:
    """Raise the right child and move its red edge to the left."""
    new_root = node.right
    assert new_root is not None
    node.right, new_root.left = new_root.left, node
    new_root.red, node.red = node.red, True
    return new_root


def rotate_right(node: RedBlackNode) -> RedBlackNode:
    """Raise the left child and transfer the incoming edge color."""
    new_root = node.left
    assert new_root is not None
    node.left, new_root.right = new_root.right, node
    new_root.red, node.red = node.red, True
    return new_root


def flip(node: RedBlackNode) -> None:
    """Move redness between the parent link and its two child links."""
    assert node.left is not None and node.right is not None
    node.red = not node.red
    node.left.red = not node.left.red
    node.right.red = not node.right.red


def repair(node: RedBlackNode) -> RedBlackNode:
    """Restore left-leaning links and dissolve a temporary four-node."""
    if red(node.right) and not red(node.left):
        node = rotate_left(node)
    if node.left is not None and red(node.left) and red(node.left.left):
        node = rotate_right(node)
    if red(node.left) and red(node.right):
        flip(node)
    return node


def insert(node: RedBlackNode | None, key: int) -> RedBlackNode:
    """Insert a red leaf and repair local links while climbing."""
    if node is None:
        return RedBlackNode(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    return repair(node)


def move_red_left(node: RedBlackNode) -> RedBlackNode:
    """Ensure the left downward step leads into a nonminimal node."""
    flip(node)
    assert node.right is not None
    if red(node.right.left):
        node.right = rotate_right(node.right)
        node = rotate_left(node)
        flip(node)
    return node


def move_red_right(node: RedBlackNode) -> RedBlackNode:
    """Ensure the right downward step leads into a nonminimal node."""
    flip(node)
    assert node.left is not None
    if red(node.left.left):
        node = rotate_right(node)
        flip(node)
    return node


def delete_min(node: RedBlackNode) -> RedBlackNode | None:
    """Remove the minimum while avoiding black-height underflow."""
    if node.left is None:
        return None
    if not red(node.left) and not red(node.left.left):
        node = move_red_left(node)
    assert node.left is not None
    node.left = delete_min(node.left)
    return repair(node)


def delete(node: RedBlackNode, key: int) -> RedBlackNode | None:
    """Remove a known-present key by moving red links before descent."""
    if key < node.key:
        assert node.left is not None
        if not red(node.left) and not red(node.left.left):
            node = move_red_left(node)
        assert node.left is not None
        node.left = delete(node.left, key)
    else:
        if red(node.left):
            node = rotate_right(node)
        if key == node.key and node.right is None:
            return None
        assert node.right is not None
        if not red(node.right) and not red(node.right.left):
            node = move_red_right(node)
        assert node.right is not None
        if key == node.key:
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.key = successor.key
            node.right = delete_min(node.right)
        else:
            node.right = delete(node.right, key)
    return repair(node)


class RedBlackTree:
    """A set of integers backed by left-leaning red-black links."""

    def __init__(self) -> None:
        self.root: RedBlackNode | None = None

    def __contains__(self, key: int) -> bool:
        node = self.root
        while node is not None:
            if node.key == key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def insert(self, key: int) -> None:
        """Insert a key and restore a black root."""
        self.root = insert(self.root, key)
        self.root.red = False

    def delete(self, key: int) -> None:
        """Remove a key if present and restore a black root."""
        if self.root is None or key not in self:
            return
        if not red(self.root.left) and not red(self.root.right):
            self.root.red = True
        self.root = delete(self.root, key)
        if self.root is not None:
            self.root.red = False
