class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        maxWords=0
        words=0
        for i in sentences:
            words=len(i.split())
            if words>maxWords:
                maxWords=words
                
        return maxWords