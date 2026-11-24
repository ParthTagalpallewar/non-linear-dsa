from .implementation import nary_node


def test_children_are_ordered_and_copied():
    child = nary_node(2)
    original = [child, nary_node(3)]
    root = nary_node(1, original)
    original.clear()
    assert [node.value for node in root.children] == [2, 3]
    assert child.children == []
