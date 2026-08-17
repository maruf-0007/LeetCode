class Solution(object):
    def maximumUnits(self, b, t):
        """
        :type boxTypes(b): List[List[int]]
        :type truckSize(t): int
        :rtype: int
        """
        b.sort(key=lambda x:x[1],reverse=1)
        s=0
        for i,j in b:
            i=min(i,t)
            s+=i*j
            t-=i
            if t==0:
                break
        return s