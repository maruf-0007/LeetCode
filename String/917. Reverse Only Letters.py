class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=""
        for i in s:
            if i in "zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP":
                a+=i
        a=a[::-1]
        x=0
        z=""
        for i in s:
            if i in "zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP":
                z+=a[x]
                x+=1
            else:
                z+=i
        return z