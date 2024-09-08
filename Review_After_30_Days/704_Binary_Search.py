class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(start_index, end_index):
            if start_index > end_index:  
                return -1
            mid_index = (start_index + end_index) // 2
            if nums[mid_index] == target:
                return mid_index
            else:
                if nums[mid_index] > target:
                    return binarySearch(start_index, mid_index-1)
                else:
                    return binarySearch(mid_index+1, end_index)
        return binarySearch(0, len(nums)-1)
    
# 时间复杂度为 O(log n)，其中 n 是数组 nums 的长度。
# 最多会递归 log₂(n) 次，因此需要 O(log n) 的空间用于存储递归调用的栈帧。