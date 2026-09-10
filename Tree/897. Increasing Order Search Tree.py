# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.ans=TreeNode(0)
        self.head=self.ans
        self.inOrder(root)
        return self.head.right

    def inOrder(self,root):
        if root is None:
            return
        self.inOrder(root.left)
        self.ans.right=root
        root.left=None
        self.ans=self.ans.right
        self.inOrder(root.right)
    