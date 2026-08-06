class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ss=sorted(s)
        st=sorted(t)
        return ss==st 