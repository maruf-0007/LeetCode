class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=-1
        nums=set(nums)
        for i in nums:
            if i*-1 in nums:
                res=max(res,i)
        return res