class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        c=0
        for i in s:
            if c==0 and i=='(':
                c+=1
            elif i=='(':
                c+=1
                res+=i
            elif c==1 and i==')':
                c-=1
            else:
                c-=1
                res+=i
        return res