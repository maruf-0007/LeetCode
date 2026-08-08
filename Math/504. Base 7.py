class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        s="-" if num<0 else ""
        num=abs(num)
        res=""
        while num:
            res=str(num%7)+res
            num//=7
        return s+res