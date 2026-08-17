class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=sorted(nums)
        res=[n.index(i) for i in nums]
        return res