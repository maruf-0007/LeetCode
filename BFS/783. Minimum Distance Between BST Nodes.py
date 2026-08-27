# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def f(n,l,h):
            if not n: return h-l
            left=f(n.left,l,n.val)
            right=f(n.right,n.val,h)
            return min(left,right)
        return f(root,float('-inf'),float('inf'))