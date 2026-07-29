class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        freq=Counter(words[0])
        for i in words:
            freq&=Counter(i)

        return list(freq.elements())