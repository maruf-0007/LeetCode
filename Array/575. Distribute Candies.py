class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        s=set(candyType)
        if len(s)<=len(candyType)/2:
            return len(s)
        return len(candyType)/2