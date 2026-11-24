from .implementation import binary_node


def test_independent_children_and_equal_values():
    child = binary_node(1)
    root = binary_node(1, left=child)
    assert root is not child
    assert root.value == child.value
    assert root.left is child and root.right is None
