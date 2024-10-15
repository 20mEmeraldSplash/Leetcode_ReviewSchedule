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
        self.result = 0
        def helper(node):
            if not node:
                return (0,0)
            robL, notRobL = helper(node.left)
            robR, notRobR = helper(node.right)
            robN = notRobL + notRobR + node.val
            notRobN = max(robL, notRobL) + max(robR, notRobR)
            return (robN, notRobN)

        return max(helper(root))