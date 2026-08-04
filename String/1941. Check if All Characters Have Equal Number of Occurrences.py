class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c=s.count(s[0])
        for i in s:
            if s.count(i)!=c:
                return False
        return True