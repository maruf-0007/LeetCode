class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)-1
        for i in range(n):
            if nums[i]==nums[i+1] or nums[i]==nums[i+2]:
                return nums[i]
        return nums[0]