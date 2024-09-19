class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)

        return max(max_sum, current_sum)
    
# 时间复杂度: O(n)，只需要遍历数组一次。
# 空间复杂度: O(1)，只使用了常数的额外空间来保存 current_sum 和 max_sum。