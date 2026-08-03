class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        c=0
        for i in range(len(s)):
            if s[i]==" ":
                c+=1
                if c==k:
                    return s[:i]
        return s