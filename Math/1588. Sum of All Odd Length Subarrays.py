class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res,freq,n=0,0,len(arr)
        for i in range(n):
            freq=freq-(i+1)//2+(n-i+1)//2
            res+=freq*arr[i]
        return res