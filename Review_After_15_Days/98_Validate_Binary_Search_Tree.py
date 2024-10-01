# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, left, right):
            if not node:
                return True
            if node.val <= left or node.val >= right:
                return False
            return helper(node.left, left, node.val) and helper(node.right, node.val, right)

        return helper(root, float('-inf'), float('inf'))