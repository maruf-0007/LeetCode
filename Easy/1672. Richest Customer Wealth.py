class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        a=0
        for i in accounts:
            a=max(a,sum(i))
        
        return a