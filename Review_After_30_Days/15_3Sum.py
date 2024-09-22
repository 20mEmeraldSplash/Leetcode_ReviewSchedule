class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        def twosum(target, nums):
            left = 0
            right = len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    self.result.append([-target, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
            
        nums = sorted(nums)
        lastchecked = float('-inf')
        for i in range(len(nums)):
            if nums[i] != lastchecked:
                twosum(-nums[i], nums[i+1: ])
                lastchecked = nums[i]
        return self.result