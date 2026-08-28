# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        s,res=[root],[]
        while s:
            node=s.pop()
            res.append(node.val)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        return res