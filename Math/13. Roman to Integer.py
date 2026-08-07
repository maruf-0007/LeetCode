class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        prev=0
        rom={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in s[::-1]:
            if rom[i]>=prev:
                res+=rom[i]
            else:
                res-=rom[i]
            prev=rom[i]
        return res        