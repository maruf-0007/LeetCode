class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i,j=len(grid)-1,0
        c=0
        while i>=0 and j<len(grid[0]):
            if grid[i][j]<0:
                c+=len(grid[0])-j
                i-=1
            else:
                j+=1
        return c