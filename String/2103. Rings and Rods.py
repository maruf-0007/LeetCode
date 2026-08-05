class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        c=0
        for i in range(10):
            i=str(i)
            if 'R'+i in rings and 'G'+i in rings and 'B'+i in rings:
                c+=1
        return c