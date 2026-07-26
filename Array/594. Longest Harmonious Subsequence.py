class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        start=0
        maxLen=0
        for i in range(len(nums)):
            while nums[i]-nums[start] >1:
                start+=1
            if nums[i]-nums[start]==1:
                maxLen=max(maxLen,i-start+1)

        return maxLen