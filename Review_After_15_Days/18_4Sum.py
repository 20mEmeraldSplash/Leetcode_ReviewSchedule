class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        def twosum(firstTwo,target, nums):
            left = 0
            right = len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    self.result.append(firstTwo+[nums[left], nums[right]])
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        nums = sorted(nums)
        
        for i in range(0, len(nums)-3):
            if i > 0 and nums[i] == nums[i - 1]:  # 去重
                continue
            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # 去重
                    continue
                twosum([nums[i], nums[j]], target-nums[i]-nums[j], nums[j+1:])
                
        return self.result
