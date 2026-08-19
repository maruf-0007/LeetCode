class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        while len(nums)>0:
            if len(nums)>1:
                c+=int(str(nums[0])+str(nums[-1]))
                del nums[-1]
            else:
                c+=nums[0]
            del nums[0]
        return c