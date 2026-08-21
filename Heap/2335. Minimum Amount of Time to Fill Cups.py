class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        m=max(amount)
        s=sum(amount)+1
        return max(m,s//2)