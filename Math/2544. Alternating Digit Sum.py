class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=0
        while n:
            res=n%10 -res
            n//=10
        return res