class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        c,l,r=0,0,len(nums)-1
        while l<r:
            if nums[l]+nums[r]<target:
                c+=r-l
                l+=1
            else:
                r-=1
        return c