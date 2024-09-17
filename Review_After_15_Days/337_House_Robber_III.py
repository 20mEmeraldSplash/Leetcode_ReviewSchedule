# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if not node:
                return (0, 0)
            left = helper(node.left)
            right = helper(node.right)
            not_rob = max(left) + max(right)
            rob = left[0] + node.val + right[0]
            return (not_rob, rob)
        return max(helper(root))