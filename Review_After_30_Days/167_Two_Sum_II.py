class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1

        result = []

        while left < right:
            total = numbers[left] + numbers[right]
            print(left, right, total)
            if total == target:
                result = [left+1, right+1]
                return result
            elif total < target:
                left += 1
            else:
                right -= 1