class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        if num1==0 or num2==0:
            return 0
        elif num1<num2:
            return self.countOperations(num2,num1)
        else:
            return num1//num2+self.countOperations(num2,num1%num2)