class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        c=0
        for i in nums:
            if i+diff in nums and i+diff*2 in nums:
                c+=1
        return c