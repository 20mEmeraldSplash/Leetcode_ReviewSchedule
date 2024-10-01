class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_sum = sum(nums)
        if num_sum % 2 != 0 :
            return False
        
        target = num_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i-num]
        return dp[-1]