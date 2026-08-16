class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        s=[]
        for i,j in enumerate(mat):
            s.append([sum(j),i])
        s.sort()
        return [k for j,k in s[0:k]]