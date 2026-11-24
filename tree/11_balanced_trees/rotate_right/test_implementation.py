from tree.avl import AVLNode

from .implementation import rotate_right


def test_rotation_preserves_order_and_refreshes_heights():
    root = rotate_right(AVLNode(3, left=AVLNode(2, left=AVLNode(1))))
    assert root.key == 2
    assert root.left is not None and root.left.key == 1
    assert root.right is not None and root.right.key == 3
    assert root.left.height == root.right.height == 1
    assert root.height == 2
