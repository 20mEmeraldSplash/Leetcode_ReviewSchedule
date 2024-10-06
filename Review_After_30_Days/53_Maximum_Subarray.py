class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [float('-inf')] * len(nums)
        dp[0] = max(dp[0], nums[0])
        result = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            result = max(result, dp[i])
            
        return result
    
# 时间复杂度: O(n)，只需要遍历数组一次。
# 空间复杂度: O(1)，只使用了常数的额外空间来保存 current_sum 和 max_sum。