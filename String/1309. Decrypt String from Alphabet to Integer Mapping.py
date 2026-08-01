class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        res=""
        while i<len(s):
            if s[i]!="#":
                res+=chr(96+int(s[i]))
            else:
                res=res[:-2]
                res+=chr(96+int(s[i-2:i]))
            i+=1
        return res