class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftmax = [0] * len(height)
        rightmax = [0] * len(height)
        leftmax[0] = height[0]
        rightmax[len(height)-1] = height[len(height)-1]
        result = 0 

        for i in range(1, len(height)):
            leftmax[i] = max(leftmax[i-1], height[i])
        for i in range(len(height) - 2, -1, -1):
            rightmax[i] = max(rightmax[i+1], height[i])
        
        
        for i in range(len(height)):
            current = max(min(leftmax[i], rightmax[i]) - height[i],0)
            result+=current
        
        return result
        

