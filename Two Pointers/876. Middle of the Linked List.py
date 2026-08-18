class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        s=f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        return s