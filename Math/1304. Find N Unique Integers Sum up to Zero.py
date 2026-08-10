class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        pairs=n//2
        for i in range(1,pairs+1):
            res.append(i)
            res.append(-i)
        if n%2!=0:
            res.append(0)
        return res