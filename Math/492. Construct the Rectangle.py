import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        x=int(math.sqrt(area))
        while area%x:
            x-=1
        return [area//x, x]