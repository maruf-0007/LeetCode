class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        arr=[]
        for i in range(len(matrix[0])):
            r=[]
            for j in range(len(matrix)):
                r.append(matrix[j][i])
            arr.append(r)
        return arr