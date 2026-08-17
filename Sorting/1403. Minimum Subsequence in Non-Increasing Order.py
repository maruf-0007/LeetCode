class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=sorted(nums)
        res=[]
        l=len(nums)
        while sum(res)<=sum(s[:l]):
            l-=1
            res.append(s[l])
        return res