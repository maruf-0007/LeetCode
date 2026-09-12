class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if len(trust)==0 and n==1:
            return 1
        c=[0]*(n+1)
        for i in trust:
            c[i[0]]-=1
            c[i[1]]+=1
        for j in range(len(c)):
            if c[j]==n-1:
                return j

        return -1