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
            
            rob_current = node.val + left[1] + right[1]
            not_rob_current = max(left) + max(right)

            return (rob_current, not_rob_current)
        return max(helper(root))