class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=len(nums)
        expectedSum=num*(num+1)//2
        actualSum=sum(nums)

        return expectedSum-actualSum