# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.res=0
        def helper(node):
            if not node:
                return 0
            left=helper(node.left)
            right=helper(node.right)
            self.res+=abs(left-right)
            return left+right+node.val
        
        helper(root)
        return self.res