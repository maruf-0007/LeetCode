class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        res=[]
        for i in range(rows):
            for j in range(cols):
                dist=abs(rCenter-i)+abs(cCenter-j)
                res.append([dist,i,j])
        res.sort()
        ans=[[i,j] for dist,i,j in res]
        return ans
        