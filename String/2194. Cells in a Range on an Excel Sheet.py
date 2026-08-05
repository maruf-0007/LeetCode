class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res=[]
        for i in range(ord(s[0]),ord(s[3])+1):
            r=""
            for j in range(int(s[1]),int(s[4])+1):
                r=chr(i)+str(j)
                res.append(r)
        return res