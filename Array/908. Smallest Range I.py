class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maX=max(nums)
        miN=min(nums)
        if maX-miN-2*k <=0:
            return 0
        else:
            return maX-miN-2*k