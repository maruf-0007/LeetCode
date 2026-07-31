class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        c=0
        for i in range(len(strs[0])):
            last="a"
            for j in strs:
                if j[i]<last:
                    c+=1
                    break
                last=j[i]
        return c