class Solution(object):
    def numWaterBottles(self, nB, nE):
        """
        :type numBottles=nB: int
        :type numExchange=nE: int
        :rtype: int
        """
        return nB+(nB-1)//(nE-1)