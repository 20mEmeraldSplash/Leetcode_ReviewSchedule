import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result = ListNode(0)
        dummy = result
        pq = []

        for l in lists:
            if l:
                heapq.heappush(pq, (l.val, l))
        
        while pq:
            smallest_val, smallest = heapq.heappop(pq)
            dummy.next = ListNode(smallest_val)
            dummy = dummy.next
            if smallest.next:
                heapq.heappush(pq, (smallest.next.val, smallest.next))
        
        return result.next