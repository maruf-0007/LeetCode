class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=sum(nums)
        for i,j in enumerate(nums):
            r-=j
            if l==r:
                return i
            l+=j
        return -1