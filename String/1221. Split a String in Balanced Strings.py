class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        ch=c=0
        for i in s:
            if i=='L':
                ch+=1
            if i=='R':
                ch-=1
            if ch==0:
                c+=1
        return c