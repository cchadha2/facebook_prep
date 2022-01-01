"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Questions:
    - Are the two nodes guaranteed to exist in the tree? Yes
    - Can the two nodes be the same node? No, they are unique


Example:
                            5
                           / \
                          4   3
                         / \ / \
                        1  7 6  8
                          /
                         9


LCA(3, 4) = 5
LCA(4, 7) = 4
LCA(9, 8) = 5


Approach:
    - Look for the two nodes in the tree using DFS
    - If one of the nodes is found, keep looking for the other as it may be a child of the found node
    - If we get to a node where the left and right DFS calls return the two given nodes, this is our LCA
    - Otherwise, the one of the nodes is a child of the other and the LCA is the more shallow node

Overall O(N) time where N is number of nodes and O(N) space for call stack at worst.
"""

def lca(root, p, q):
    if not root:
        return

    left = lca(root.left, p, q)
    # We've found our LCA.
    if left and left is not p and left is not q:
        return left

    right = lca(root.right, p, q)
    # We've found our LCA.
    if right and right is not p and right is not q:
        return right

    # This is the LCA if both left and right are p and q.
    if left and right:
        return root

    return root if root is p or root is q else left or right
