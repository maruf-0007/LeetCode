class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s=[]
        s1=s1.split()
        s2=s2.split()
        for i in s1:
            if i not in s2:
                if s1.count(i)==1:
                    s.append(i)
        for i in s2:
            if i not in s1:
                if s2.count(i)==1:
                    s.append(i)
        return s