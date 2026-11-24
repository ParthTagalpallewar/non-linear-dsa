# Balanced Trees

An AVL tree caches subtree heights and limits their difference to one.
A red-black tree colors links so no red link follows another red link and
all root-to-null paths have the same black count. The implementation here
also leans red links to the left, encoding two- and three-key choices as
small binary shapes. Rotations rearrange a constant number of links while
preserving inorder order. AVL updates repair height differences on descent
return. Red-black deletion moves red links toward the path before descent
so removing a key cannot drop the path's black count unexpectedly.

Complete implementations: [AVL](../avl.py) and [left-leaning red-black](../red_black.py).

## Lessons

- [ ] [Left Rotation](rotate_left/README.md) · P2
- [ ] [Right Rotation](rotate_right/README.md) · P2
- [ ] [Left–Right Rotation](rotate_left_right/README.md) · P2
- [ ] [Right–Left Rotation](rotate_right_left/README.md) · P2
- [ ] [AVL Tree](avl_tree/README.md) · P2
- [ ] [AVL Tree Insertion and Deletion](avl_updates/README.md) · P2
- [ ] [Red-Black Tree](red_black_tree/README.md) · P3
- [ ] [Red-Black Tree Insertion and Deletion](red_black_updates/README.md) · P3
- [ ] [AVL Tree Insertion](avl_insert/README.md) · P2
- [ ] [AVL Tree Deletion](avl_delete/README.md) · P2
- [ ] [Red-Black Tree Insertion](red_black_insert/README.md) · P3
- [ ] [Red-Black Tree Deletion](red_black_delete/README.md) · P3
