class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        x=list(s)
        for i in range(len(s)//2):
            x[i]=x[~i]=min(x[i],x[~i])
        return ''.join(x)