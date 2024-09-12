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
        # 将 max_sum 设置为实例的属性
        self.max_sum = float('-inf')

        def helper(node):
            if not node:
                return 0
            leftNodeSum = max(helper(node.left), 0)
            rightNodeSum = max(helper(node.right), 0)

            currentNodeSum = node.val + leftNodeSum + rightNodeSum

            self.max_sum = max(self.max_sum,currentNodeSum )

            return node.val + max(leftNodeSum, rightNodeSum)
        
        helper(root)
        return self.max_sum