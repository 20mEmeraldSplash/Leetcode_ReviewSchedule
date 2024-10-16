class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        n = len(nums)

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1,n - 2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                t = target - nums[i]- nums[j] 
                left = j + 1
                right = n - 1
                while left < right:
                    if nums[left] + nums[right] == t:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left + 1] == nums[left]:
                            left += 1
                        while right > left and nums[right-1] == nums[right]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] > t: 
                        right -= 1
                    else:
                        left += 1

        return result

        
            
