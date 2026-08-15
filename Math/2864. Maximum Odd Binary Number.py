class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=sorted(s)
        s=s[:-1]
        s=s[::-1]
        s.append('1')
        return "".join(s)