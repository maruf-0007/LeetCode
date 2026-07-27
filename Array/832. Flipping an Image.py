class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        for i in image:
            i.reverse()
            res.append([x^1 for x in i])

        return res