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
        pq = []
        dummy = ListNode(0)
        current = dummy

        for l in lists:
            if l:
                heapq.heappush(pq, (l.val, l))
        
        while pq:
            node_val, node = heapq.heappop(pq)
            current.next = ListNode(node_val)
            current = current.next

            if node.next:
                heapq.heappush(pq, (node.next.val, node.next))
        
        return dummy.next