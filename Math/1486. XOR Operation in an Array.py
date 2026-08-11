class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        res=0
        while n:
            res^=start
            start+=2
            n-=1
        return res