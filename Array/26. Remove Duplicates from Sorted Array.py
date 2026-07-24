class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dup=0
        size=len(nums)
        for i in range(1,size):
            if nums[i]==nums[i-1]:
                dup+=1
            else:
                nums[i-dup]=nums[i]

        return size-dup