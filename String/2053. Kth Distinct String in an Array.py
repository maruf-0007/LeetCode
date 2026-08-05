class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        x=[]
        for i in arr:
            if arr.count(i)<2:
                x.append(i)
        for i in arr:
            if i in x:
                k-=1
            if k==0:
                return i
        return ""