class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        if nums[0]>=n:
            return n
        for i in range(1,n):
            if nums[n-i]>=i and nums[n-i-1]<i:
                return i
        return -1