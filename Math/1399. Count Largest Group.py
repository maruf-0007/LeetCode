class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr=[0]*37
        for i in range(1,n+1):
            num=i
            Sum=0
            while num:
                Sum+=num%10
                num//=10
            arr[Sum]+=1
        maxi=max(arr)
        return arr.count(maxi)