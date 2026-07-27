class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        res=0
        for i in range(len(points)):
            a,b=points[i]
            for j in range(i+1, len(points)):
                c,d=points[j]
                for k in range(j+1, len(points)):
                    e,f=points[k]
                    res=max(res,abs(a*(d-f)+c*(f-b)+e*(b-d))/2.0)

        return res