class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=b=0
        for i in nums:
            if a<=i:
                b=a
                a=i
            elif b<i:
                b=i
        return (a-1)*(b-1)