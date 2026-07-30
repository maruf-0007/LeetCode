class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        origin=[0,0]
        for i in moves:
            if i=="U":
                origin[0]+=1
            if i=="D":
                origin[0]-=1
            if i=="R":
                origin[1]+=1
            if i=="L":
                origin[1]-=1

        return origin==[0,0]
            