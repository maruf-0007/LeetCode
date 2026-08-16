class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c=Counter(nums1)
        res=[]
        for i in nums2:
            if c[i]>0:
                res.append(i)
                c[i]-=1
        return res