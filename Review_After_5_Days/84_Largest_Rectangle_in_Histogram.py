class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        checked = []
        result = 0
        for i in range(len(heights)):
            while checked and heights[i] < heights[checked[-1]]:
                check_index = checked.pop()
                h = heights[check_index]
                w = i - checked[-1] - 1 if checked else i
                result = max(result, h * w)
                
            checked.append(i)
        return result
