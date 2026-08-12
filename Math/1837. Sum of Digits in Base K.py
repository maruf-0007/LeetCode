class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        Sum=0
        while n>0:
            Sum+=n%k
            n//=k
        return Sum