class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        i=0
        j=len(s)
        res=[]
        for k in range(len(s)):
            if s[k]=="I":
                res.append(i)
                i+=1
            elif s[k]=="D":
                res.append(j)
                j-=1
        res.append(j)
        return res