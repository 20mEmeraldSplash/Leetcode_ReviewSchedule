class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        check = [(heights[0], 0)]
        result = 0
        for i in range(1, len(heights)):
            if heights[i] >= check[-1][0]:
                check.append((heights[i], i))
            else:
                while check and heights[i] < check[-1][0]:
                    height, left_index = check.pop(-1)
                    width = i if not check else i - check[-1][1] - 1 #有点难
                    result = max(result, height * width)
                check.append((heights[i], i))
        return result