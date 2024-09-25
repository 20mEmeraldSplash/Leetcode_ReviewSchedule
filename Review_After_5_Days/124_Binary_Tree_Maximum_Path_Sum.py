# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = float('-inf')
        def helper(node):
            if not node:
                return 0
            left_val = max(helper(node.left),0)
            right_val = max(helper(node.right),0)
            current_sum = left_val + right_val + node.val
            self.result = max(self.result, current_sum)
            return node.val+max(left_val, right_val)
        helper(root)
        return self.result