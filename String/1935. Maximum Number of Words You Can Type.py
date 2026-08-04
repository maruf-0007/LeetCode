class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        s=text.split()
        c=0
        for i in s:
            for j in brokenLetters:
                if j in i:
                    break
            else:
                c+=1
        return c