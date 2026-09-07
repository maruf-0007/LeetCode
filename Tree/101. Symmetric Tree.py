# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isSym(p,q):
            if not p and not q:
                return True
            if p and q and p.val==q.val:
                return isSym(p.left,q.right) and isSym(p.right,q.left)
            return False

        return isSym(root,root)