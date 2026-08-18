class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        pos=[]
        for i in range(len(s)):
            if s[i]==c:
                pos.append(i)
        res=[]
        for i in range(len(s)):
            temp=[]
            for j in pos:
                temp.append(abs(i-j))
            res.append(min(temp))
        return res