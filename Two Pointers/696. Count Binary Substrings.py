class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans,p,c=0,0,1
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                ans+=min(p,c)
                p=c
                c=1
            else:
                c+=1
        ans+=min(p,c)
        return ans