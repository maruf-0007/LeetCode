# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res=0
        s=[(root,False)]
        while s:
            curr,l=s.pop()
            if not curr:
                continue
            if not curr.left and not curr.right:
                if l:
                    res+=curr.val
            else:
                s.append((curr.left,True))
                s.append((curr.right,False))
        return res