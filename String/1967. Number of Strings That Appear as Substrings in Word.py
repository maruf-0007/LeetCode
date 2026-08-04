class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        res=0
        for i in patterns:
            if word.find(i)!=-1:
                res+=1
        return res