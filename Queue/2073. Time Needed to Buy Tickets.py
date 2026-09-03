class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        t=0
        for i,j in enumerate(tickets):
            if i<=k:
                t+=min(tickets[i],tickets[k])
            else:
                t+=min(tickets[i],tickets[k]-1)
        
        return t