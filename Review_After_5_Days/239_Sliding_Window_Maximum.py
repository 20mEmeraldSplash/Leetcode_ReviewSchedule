import heapq
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        pq = []
        result = []

        for i in range(len(nums)):
            heapq.heappush(pq,(-nums[i], i))
            if i >= k-1:
                while pq[0][1] <= i-k:
                    heapq.heappop(pq) #弹出并返回 heap 的最小的元素，保持堆的不变性
                result.append(-pq[0][0])

        return result