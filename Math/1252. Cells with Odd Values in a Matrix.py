class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        row=[0]*m
        col=[0]*n
        for i in indices:
            row[i[0]]=row[i[0]]+1
            col[i[1]]=col[i[1]]+1
        c=0
        for j in range(m):
            for k in range(n):
                val=row[j]+col[k]
                if val%2!=0:
                    c+=1
        return c