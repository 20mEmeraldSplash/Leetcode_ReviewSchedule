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
        dummy = ListNode(0)
        current = dummy
        pq=[]
        
        for l in lists:
            if l:
                heapq.heappush(pq, (l.val, l))
        while pq:
            node_val, node = heapq.heappop(pq)
            if node.next:
                heapq.heappush(pq, (node.next.val, node.next))
            current.next = node
            current = current.next
        return dummy.next