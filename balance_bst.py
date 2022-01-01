"""
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.



Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]


Questions:
    - Define balanced? Depth of two subtrees of every node never differs by more than 1
    - Can give any balanced tree answer
    - Dont have to reuse the original nodes but I will
    - Are we guaranteed to get a balanced tree? No

Example:

Unbalanced:
                        2
                         \
                          5
                           \
                            7
                             \
                              9
                               \
                                12
                                 \
                                  15
                                   \
                                    17
N = 7

Balanced:
                        9
                       / \
                      5   15
                     / \  / \
                    2  7 12 17


Approach:
    - Do an inorder traversal and get a list of the nodes sorted by their values (O(N) time and space) through DFS.
      If tree is already balanced, do nothing.
    - Recursively divide the list in two on either side of a midpoint which will be your next root
    - This is guaranteed to be a balanced tree?
    - Need a function to check if tree is balanced?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        nodes = []
        balanced_tree = True

        # O(N) time and space for nodes list and call stack.
        def inorder(node):
            if not node:
                return 0

            max_left = inorder(node.left)

            nodes.append(node)

            max_right = inorder(node.right)

            if abs(max_right - max_left) > 1:
                nonlocal balanced_tree
                balanced_tree = False

            return max(max_left, max_right) + 1

        # O(N) time and O(logN) space for divide and conquer approach.
        def build_tree(start, end):
            if start > end:
                return
            elif start == end:
                nodes[start].left = nodes[start].right = None
                return nodes[start]

            mid = (start + end) // 2
            node = nodes[mid]

            node.left = build_tree(start, mid - 1)
            node.right = build_tree(mid + 1, end)

            return node


        inorder(root)
        return build_tree(0, len(nodes) - 1) if not balanced_tree else root
