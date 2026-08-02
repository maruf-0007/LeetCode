class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s=set()
        for i in words:
            for j in words:
                if i!=j and i in j:
                    s.add(i)

        return list(s)