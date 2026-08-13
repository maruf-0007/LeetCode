class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        a=sorted(str(num))
        return int(a[0]+a[2])+int(a[1]+a[3])