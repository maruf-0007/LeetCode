class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr=[]
        for i in range(numRows):
            if i==0:
                prev=[1]
                arr.append(prev)
            else:
                curr=[1]
                j=1
                while(j<i):
                    curr.append(prev[j-1]+prev[j])
                    j+=1

                curr.append(1)
                arr.append(curr)
                prev=curr

        return arr