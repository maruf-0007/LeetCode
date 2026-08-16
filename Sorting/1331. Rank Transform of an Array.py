class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if not arr:
            return []
        sort=sorted(set(arr))
        s={}
        for i,j in enumerate(sort,1):
            s[j]=i
        return [s[j] for j in arr]