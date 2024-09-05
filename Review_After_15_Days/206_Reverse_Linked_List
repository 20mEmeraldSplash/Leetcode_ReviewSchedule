# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
    
# 时间复杂度: O(n)，其中 n 是链表的长度。我们需要遍历每个节点一次。
# 空间复杂度: O(1)，因为我们只使用了常数个额外指针，空间消耗不随着链表长度增长。