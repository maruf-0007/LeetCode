class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        s=sum(int(i) for i in str(num))
        if s%2==0:
            return num//2
        else:
            return (num-1)//2