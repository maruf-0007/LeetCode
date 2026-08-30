# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        res=0
        q=[root]
        while q:
            node=q.pop()
            if node:
                if low<=node.val<=high:
                    res+=node.val
                if node.val>low:
                    q.append(node.left)
                if node.val<high:
                    q.append(node.right)
        return res