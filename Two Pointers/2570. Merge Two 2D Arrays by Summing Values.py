class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        s={}
        for i,j in nums1:
            s[i]=s.get(i,0)+j
        for i,j in nums2:
            s[i]=s.get(i,0)+j
        return sorted(s.items())