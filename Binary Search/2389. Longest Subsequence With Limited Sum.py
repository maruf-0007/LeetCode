class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res=[]
        for i in queries:
            c,v=0,0
            for j in nums:
                if v+j<=i:
                    c+=1
                    v+=j
            res.append(c)
        return res