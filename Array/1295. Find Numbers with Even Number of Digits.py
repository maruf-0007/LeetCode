class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in nums:
            d=0
            n=i
            if n<10:
                d=1
                continue
            while n>0:
                n//=10
                d+=1
            if d%2==0:
                c+=1
        return c