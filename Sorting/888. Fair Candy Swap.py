class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        d=(sum(aliceSizes)-sum(bobSizes))/2
        a=set(aliceSizes)
        for i in set(bobSizes):
            if d+i in a:
                return [d+i,i]
        