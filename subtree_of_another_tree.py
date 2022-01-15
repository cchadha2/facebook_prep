# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check_structure(node, subroot_node):
            node_stack = [node]
            subroot_stack = [subroot_node]

            while node_stack and subroot_stack:
                node1 = node_stack.pop()
                node2 = subroot_stack.pop()

                if node1.val != node2.val:
                    return False

                if ((node1.left and not node2.left)
                     or (node2.left and not node1.left)):
                    return False

                if node1.left:
                    node_stack.append(node1.left)
                if node1.right:
                    node_stack.append(node1.right)

                if node2.left:
                    subroot_stack.append(node2.left)
                if node2.right:
                    subroot_stack.append(node2.right)

            return not node_stack and not subroot_stack


        stack = [root]

        while stack:
            node = stack.pop()

            if node.val == subRoot.val and check_structure(node, subRoot):
                return True

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False
