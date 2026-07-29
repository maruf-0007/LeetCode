class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        countt=0
        n=sorted(heights)
        for i in range(len(heights)):
            if heights[i]!=n[i]:
                countt+=1
        return countt