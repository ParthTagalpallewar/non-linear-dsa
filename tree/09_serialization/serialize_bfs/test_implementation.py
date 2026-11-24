import pytest

from tree.nodes import BinaryNode

from .implementation import deserialize_bfs, serialize_bfs


def test_round_trip_preserves_shape_and_values():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4)), BinaryNode(3))
    assert serialize_bfs(root) == "1,2,3,4,#,#,#,#,#"
    restored = deserialize_bfs(serialize_bfs(root))
    assert restored is not root
    assert serialize_bfs(restored) == "1,2,3,4,#,#,#,#,#"
    assert deserialize_bfs(serialize_bfs(None)) is None
    assert serialize_bfs(deserialize_bfs("-4,#,#")) == "-4,#,#"


def test_rejects_truncated_and_trailing_data():
    for data in ("1,#", "#,#", ""):
        with pytest.raises(ValueError):
            deserialize_bfs(data)
