# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        temp=ListNode(0)
        temp.next=head
        pre,cur=temp,head
        while cur:
            if cur.val==val:
                pre.next=cur.next
            else:
                pre=cur
            cur=cur.next
        return temp.next