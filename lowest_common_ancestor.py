"""
2 cases:
    - LCA is a node that is not p or q
    - LCA is one of p or q

The second case means that we must continue to search the tree even after finding p or q as one might be a descendent of the other.

Example:

       3
     /   \
    5     6
   / \
  7   4

LCA(7, 4) = 5
LCA(5, 4) = 5

Approach:
    - Traverse the tree, looking for p and q
    - If either is found, continue to search for the other and finally return p or q from themselves if found (after the search their own subtrees)
    - If the LCA is neither p nor q, return it up to the root and to the original call
    - Otherwise, propagate p or q (whichever is the LCA) to the root and to the original call

O(N) time as we must search the entire tree.
Between O(logN) and O(N) space for the call stack depending on if tree is balanced or not.
"""


def lca(root, p, q):
    if not root:
        return

    left = lca(root.left, p, q)
    if left and not left is p and not left is q:
        return left

    right = lca(root.right, p, q)
    if right and not right is p and not right is q:
        return right

    if (left and right) or root is p or root is q:
        return root
    else:
        return left or right
