class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        result = cost
        for i in range(2, len(cost)):
            result[i] += min(cost[i-1], cost[i-2])
             
        return min(result[-1], result[-2])