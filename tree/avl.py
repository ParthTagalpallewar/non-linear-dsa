"""AVL nodes, rotations, and updates."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AVLNode:
    """A search node with cached height measured in nodes."""

    key: int
    left: AVLNode | None = None
    right: AVLNode | None = None
    height: int = 1


def height(node: AVLNode | None) -> int:
    """Return a cached height, with zero for an empty subtree."""
    return node.height if node is not None else 0


def refresh(node: AVLNode) -> None:
    """Recalculate height from the current children."""
    node.height = 1 + max(height(node.left), height(node.right))


def rotate_left(node: AVLNode) -> AVLNode:
    """Raise the right child and transfer its left subtree."""
    new_root = node.right
    if new_root is None:
        raise ValueError("left rotation requires a right child")
    node.right, new_root.left = new_root.left, node
    refresh(node)
    refresh(new_root)
    return new_root


def rotate_right(node: AVLNode) -> AVLNode:
    """Raise the left child and transfer its right subtree."""
    new_root = node.left
    if new_root is None:
        raise ValueError("right rotation requires a left child")
    node.left, new_root.right = new_root.right, node
    refresh(node)
    refresh(new_root)
    return new_root


def rotate_left_right(node: AVLNode) -> AVLNode:
    """Rotate the left child left and then rotate the parent right."""
    if node.left is None:
        raise ValueError("left-right rotation requires a left child")
    node.left = rotate_left(node.left)
    return rotate_right(node)


def rotate_right_left(node: AVLNode) -> AVLNode:
    """Rotate the right child right and then rotate the parent left."""
    if node.right is None:
        raise ValueError("right-left rotation requires a right child")
    node.right = rotate_right(node.right)
    return rotate_left(node)


def balance(node: AVLNode) -> AVLNode:
    """Repair one modified subtree after its children have been repaired."""
    refresh(node)
    difference = height(node.left) - height(node.right)
    if difference > 1:
        assert node.left is not None
        if height(node.left.right) > height(node.left.left):
            return rotate_left_right(node)
        return rotate_right(node)
    if difference < -1:
        assert node.right is not None
        if height(node.right.left) > height(node.right.right):
            return rotate_right_left(node)
        return rotate_left(node)
    return node


def insert(node: AVLNode | None, key: int) -> AVLNode:
    """Insert a key, ignoring duplicates."""
    if node is None:
        return AVLNode(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    return balance(node)


def delete(node: AVLNode | None, key: int) -> AVLNode | None:
    """Delete a key if present and rebalance on the return path."""
    if node is None:
        return None
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    elif node.left is None:
        return node.right
    elif node.right is None:
        return node.left
    else:
        replacement = node.right
        while replacement.left is not None:
            replacement = replacement.left
        node.key = replacement.key
        node.right = delete(node.right, replacement.key)
    return balance(node)


class AVLTree:
    """A set of integers backed by an AVL tree."""

    def __init__(self) -> None:
        self.root: AVLNode | None = None

    def insert(self, key: int) -> None:
        """Insert a key if absent."""
        self.root = insert(self.root, key)

    def delete(self, key: int) -> None:
        """Delete a key if present."""
        self.root = delete(self.root, key)

    def __contains__(self, key: int) -> bool:
        node = self.root
        while node is not None:
            if node.key == key:
                return True
            node = node.left if key < node.key else node.right
        return False
