class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        c=0
        for i in nums:
            if i%2==0 and i%3==0:
                s+=i
                c+=1
        if c==0:
            return c
        return s//c