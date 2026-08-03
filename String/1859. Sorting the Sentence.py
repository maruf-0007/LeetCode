class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        strr=s[::-1].split()
        strr.sort()
        for i in strr:
            res.append(i[1:][::-1])
        return " ".join(res)