# BST vs AVL vs red-black tree

| Property | Plain BST | AVL | Left-leaning red-black |
| --- | --- | --- | --- |
| Additional invariant | Strict key order | Child heights differ by at most one | Equal black counts, no consecutive red links, red links lean left |
| Node metadata | Key and children | Cached height | Color of incoming link |
| Search | O(H + 1) | O(log(N + 1)) | O(log(N + 1)) |
| Insert/delete | O(H + 1) | O(log(N + 1)) | O(log(N + 1)) |
| Degenerate sorted inserts | Can create a chain | Rotate to repair imbalance | Rotate and recolor to maintain invariants |
| Useful when | Input is small or shape is controlled | Frequent lookups benefit from a stricter height bound | Repeated changes need guaranteed logarithmic height |

N is the number of stored keys, and H is the actual height. AVL tracks the
height of every subtree. Red-black balance comes from the facts that black
counts match and any red link must be followed by a black link. That
allows a root-to-null path to be at most twice as long as the shortest
one. Rotations preserve inorder key order in both structures, and
deletions may require several local repairs.

Read the [BST lessons](10_binary_search_tree/README.md) and
[balanced trees with invariant tests](11_balanced_trees/README.md).
