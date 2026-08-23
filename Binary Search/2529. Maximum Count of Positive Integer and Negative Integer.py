class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a,b=0,0
        for i in nums:
            if i<0:
                a+=1
            elif i>0:
                b+=1
        return max(a,b)