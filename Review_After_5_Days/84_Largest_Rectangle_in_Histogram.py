class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        result = 0
        checked = [0]
        
        for i in range(len(heights)):
            if heights[i] >= heights[checked[-1]]:
                checked.append(i)
            else:
                while checked and heights[i] < heights[checked[-1]]:
                    h = heights[checked.pop(-1)]
                    w = i if not checked else i - checked[-1] - 1
                    result = max(result, h * w)
                checked.append(i)
        return result

        return result
