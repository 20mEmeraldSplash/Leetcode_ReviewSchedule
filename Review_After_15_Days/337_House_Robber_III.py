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
            rob_left, not_rob_left = helper(node.left)
            rob_right, not_rob_right = helper(node.right)
            rob = not_rob_left + not_rob_right + node.val
            not_rob = max(rob_left, not_rob_left) + max(rob_right, not_rob_right )
            return (rob, not_rob)
        return max(helper(root))