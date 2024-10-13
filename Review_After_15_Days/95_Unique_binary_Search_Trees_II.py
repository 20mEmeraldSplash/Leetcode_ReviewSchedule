# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def helper(start, end):
            if start > end:
                return [None]
            all_trees = []
            for i in range(start, end+1):
                leftTree = helper(start, i-1)
                rightTree = helper(i+1, end)

                for l in leftTree:
                    for r in rightTree:
                        newTree = TreeNode(i)
                        newTree.left = l
                        newTree.right = r
                        all_trees.append(newTree)
            return all_trees
        return helper(1, n)

            