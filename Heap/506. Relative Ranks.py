class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        c=sorted(score,reverse=True)
        rank={}
        for i in range(len(c)):
            if i == 0:
                rank[c[i]]="Gold Medal"
            elif i == 1:
                rank[c[i]]="Silver Medal"
            elif i == 2:
                rank[c[i]]="Bronze Medal"
            else:
                rank[c[i]]=str(i+1)
        return [rank[x] for x in score]