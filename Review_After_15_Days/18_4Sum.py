class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        for i in range(0, len(nums) - 3):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, len(nums) - 2):
                if j > i + 1 and nums[j-1] == nums[j]:
                    continue
                curr_target = target - nums[i] - nums[j]
                left = j+1
                right = len(nums) - 1

                while left < right:
                    curr_sum = nums[left] + nums[right]
                    if curr_sum == curr_target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                    
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left <right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif curr_sum < curr_target:
                        left += 1
                    else:
                        right -= 1
        return result