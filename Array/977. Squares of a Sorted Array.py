class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sq=[i*i for i in nums]
        sq.sort()
        return sq