class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        c="abcdefghijklmnopqrstuvwxyz"
        while s:
            for i in c:
                if i in s:
                    res.append(i)
                    s=s.replace(i,"",1)
                else:
                    c=c.replace(i,"")
            c=c[::-1]
        return "".join(res)