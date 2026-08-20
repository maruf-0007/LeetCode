class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        nums.sort()
        ans=999999999
        i,j=0,len(nums)-1
        while i<=j:
            ans=min(ans,(nums[i]+nums[j])/2.0)
            i+=1
            j-=1
        return ans