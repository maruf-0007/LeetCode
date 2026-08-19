class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        n=len(arr2)
        arr2.sort()
        res=0
        for i in arr1:
            l,h=0,n-1
            while l<=h:
                mid=(l+h)//2
                if abs(i-arr2[mid])<=d:
                    break
                elif i<arr2[mid]:
                    h=mid-1
                else:
                    l=mid+1
            else:
                res+=1
        return res