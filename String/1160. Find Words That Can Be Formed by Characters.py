class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res=0
        for i in words:
            flag=1
            for j in i:
                if chars.count(j)<i.count(j):
                    flag=0
                    break
            if flag:
                res+=len(i)
        return res