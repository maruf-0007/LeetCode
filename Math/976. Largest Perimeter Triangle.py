class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        nums.reverse()
        n=len(nums)
        for i in range(1,n-1):
            a,b,c=nums[i+1],nums[i],nums[i-1]
            if a+b>c:
                return a+b+c
        return 0