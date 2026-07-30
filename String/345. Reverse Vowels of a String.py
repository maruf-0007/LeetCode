class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel=[]
        for i in s:
            if i in "aeiouAEIOU":
                vowel.append(i)
        res=""
        for i in s:
            if i in "aeiouAEIOU":
                res+=vowel.pop()
            else:
                res+=i
        return res