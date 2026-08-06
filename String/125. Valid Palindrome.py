class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res=[]
        for i in s:
            if i.isalnum():
                res.append(i.lower())
        return res==res[::-1]