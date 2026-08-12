class Solution(object):
    def countBalls(self, l, h):
        """
        :type lowLimit=l: int
        :type highLimit=h: int
        :rtype: int
        """
        box=[0]*100
        for i in range(l,h+1):
            box[sum([int(j) for j in str(i)])]+=1

        return max(box)