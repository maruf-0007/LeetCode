class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        s=0
        for i in range(len(grid[0])):
            a=0
            for j in grid:
                m=max(j)
                if m>a:
                    a=m
                j.remove(m)
            s+=a
        return s