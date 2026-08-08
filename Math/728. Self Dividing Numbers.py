class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res=[]
        for i in range(left,right+1):
            m=i
            s=True
            while m:
                d=m%10
                if d==0 or i%d:
                    s=False
                    break
                m//=10
            if s:
                res.append(i)
        return res