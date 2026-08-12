class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        w=n//7
        d=n%7
        total=28*w+(w*(w-1)*7)//2
        
        start=w+1
        total+=(2*start+(d-1))*d//2
        return total