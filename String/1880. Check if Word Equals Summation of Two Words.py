class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        arr=[firstWord, secondWord, targetWord]
        s=[]
        for i in arr:
            s.append(self.calcSum(i))
        return s[0]+s[1]==s[2]
    def calcSum(self, i):
        st=""
        for j in i:
            st+=str(ord(j)-97)
        return int(st)