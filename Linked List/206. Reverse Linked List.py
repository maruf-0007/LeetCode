# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pre,cur=None,head
        while cur:
            temp=cur.next
            cur.next=pre #reverse
            pre=cur
            cur=temp
        return pre