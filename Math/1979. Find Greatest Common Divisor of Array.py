class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Min=min(nums)
        Max=max(nums)
        while Max!=0:
            Min,Max=Max,Min%Max
        return Min