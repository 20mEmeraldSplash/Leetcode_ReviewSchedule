class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total//2
        memo = {}

        def helper(current_sum, index):
            if (current_sum, index) in memo:
                return memo[(current_sum, index)]
            if current_sum == target:
                return True
            if current_sum > target or index >= len(nums):
                return False
            result = helper(current_sum+nums[index], index+1) or helper(current_sum, index+1)
            memo[(current_sum, index)] = result
            return result
            
        return helper(0, 0)