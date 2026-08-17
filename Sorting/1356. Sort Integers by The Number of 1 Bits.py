class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        s=[]
        for i in arr:
            c=bin(i)[2:].count("1")
            s.append([c,i])
        s.sort()
        arr=[j for i,j in s]
        return arr