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
        def helper(node, small, large):
            if not node: 
                return True
            if not (small < node.val < large):
                return False
            return helper(node.left, small, node.val) and helper(node.right, node.val, large)
        return helper(root, float('-inf'), float('inf'))
