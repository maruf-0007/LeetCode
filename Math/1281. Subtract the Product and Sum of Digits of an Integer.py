class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        summ=0
        pro=1
        while n>0:
            d=n%10
            summ+=d
            pro*=d
            n=n//10
        return pro-summ