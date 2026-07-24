class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        List=[]
        start=1
        List.append(start)
        for i in range(rowIndex):
            start*=(rowIndex-i)
            start//=(i+1)
            List.append(start)

        return List