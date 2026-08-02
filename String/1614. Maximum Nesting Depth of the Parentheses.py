class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        n=0
        for i in s:
            if i=="(":
                c+=1
                n=max(c,n)
            elif i==")":
                c-=1
            else:
                continue
        return n