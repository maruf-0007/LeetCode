# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def res(node,l,h):
            if not node:
                return h-l
            left=res(node.left,l,node.val)
            right=res(node.right,node.val,h)
            return min(left,right)
        
        return res(root,float('-inf'),float('inf'))