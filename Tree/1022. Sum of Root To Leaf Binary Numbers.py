# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def sumRootLeaf(root,val):
            if not root:
                return 0
            val=val*2+root.val
            if not root.left and not root.right:
                return val
            return sumRootLeaf(root.left,val) + sumRootLeaf(root.right,val)
        return sumRootLeaf(root,0)