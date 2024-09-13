# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        self.result = []
        
        def helper(node, k):
            if not node:
                return
            if k == 0:
                self.result.append(node.val)
                return
            helper(node.left, k-1)
            helper(node.right, k-1)

        def dfs(node):
            if not node:
                return -1
            if node == target:
                helper(node, k)
                return 0
            left_distance = dfs(node.left)
            if left_distance != -1:
                if left_distance + 1 == k:
                    self.result.append(node.val)
                else:
                    if k - left_distance - 2 >= 0:
                        helper(node.right, k - left_distance - 2)
                return left_distance + 1

            right_distance = dfs(node.right)
            if right_distance != -1:
                if right_distance + 1 == k:
                    self.result.append(node.val)
                else:
                    if k - right_distance - 2 >= 0:
                        helper(node.left, k - right_distance - 2)
                return right_distance + 1

            return -1
        
        dfs(root)
        
        return self.result