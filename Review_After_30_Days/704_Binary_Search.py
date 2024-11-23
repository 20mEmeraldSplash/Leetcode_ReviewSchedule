class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def helper(start, end):
            if start > end:
                return -1
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return helper(mid + 1, end)
            else:
                return helper(start, mid - 1)

        return helper(0, len(nums) - 1)
# 时间复杂度为 O(log n)，其中 n 是数组 nums 的长度。
# 最多会递归 log₂(n) 次，因此需要 O(log n) 的空间用于存储递归调用的栈帧。