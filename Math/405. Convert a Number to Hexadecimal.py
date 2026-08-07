class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        res=""
        hexa="0123456789abcdef"
        if num==0:
            return "0"
        elif num<0:
            num+=2**32
        while num:
            res=hexa[num%16]+res
            num//=16
        return res