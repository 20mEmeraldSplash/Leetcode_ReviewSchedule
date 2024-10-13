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
        # 距离node为k的节点
        def helperI(node, k):
            if not node:
                return
            if k == 0:
                self.result.append(node.val)
                return
            helperI(node.left, k-1)
            helperI(node.right, k-1)
        
        # 计算每个节点距离target的距离
        def dfs(node):
            if not node:
                return -1
            if node.val == target.val:
                helperI(node, k)
                return 0
            leftD = dfs(node.left)
            if leftD != -1:
                if leftD + 1 == k:
                    self.result.append(node.val)
                helperI(node.right, k-leftD-2)
                return leftD + 1
            rightD = dfs(node.right)
            if rightD != -1:
                if rightD + 1 == k:
                    self.result.append(node.val)
                helperI(node.left, k-rightD-2)
                return rightD + 1
            return -1

        dfs(root)
        return self.result