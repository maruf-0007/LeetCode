class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        s1=Counter(ransomNote)
        s2=Counter(magazine)
        if s1 & s2==s1:
            return True
        return False