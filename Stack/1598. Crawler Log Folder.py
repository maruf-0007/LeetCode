class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        dep=0
        for i in logs:
            if i=="../":
                if dep>0:
                    dep-=1
            elif i=="./":
                continue
            else:
                dep+=1
        return dep 