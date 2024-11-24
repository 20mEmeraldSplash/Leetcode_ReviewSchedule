import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        result = ListNode(0)
        dummy = result
        pq = []

        for l in lists:
            if l:
                heapq.heappush(pq, (l.val, l))
        
        while pq:
            checkVal, checkNode = heapq.heappop(pq)
            dummy.next = ListNode(checkVal)
            dummy = dummy.next
            if checkNode.next:
                heapq.heappush(pq, (checkNode.next.val, checkNode.next))

        return result.next
        