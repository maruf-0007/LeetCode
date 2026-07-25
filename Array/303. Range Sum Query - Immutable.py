class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum=[]
        j=0
        for i in nums:
            j+=i
            self.sum.append(j)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left>0 and right>0:
            return self.sum[right]-self.sum[left-1]
        else:
            return self.sum[left or right]

