class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k=k
        self.heap=[]
        for i in nums:
            self.add(i)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
        elif val>self.heap[0]:
            heapq.heapreplace(self.heap,val)
        return self.heap[0]