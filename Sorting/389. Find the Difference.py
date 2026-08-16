class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ss=sorted(s)
        ts=sorted(t)
        i=0
        while i<len(ss) and ss[i]==ts[i]:
            i+=1
        return ts[i]