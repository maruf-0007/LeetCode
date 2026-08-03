class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c=0
        m=len(s)/2
        for i,j in enumerate(s):
            if j in "aeiouAEIOU":
                c+=1 if i<m else -1

        return c==0