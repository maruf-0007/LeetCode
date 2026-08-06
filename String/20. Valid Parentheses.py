class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p={')': '(', '}': '{', ']': '['}
        res=[]
        for i in s:
            if i in p.values():
                res.append(i)
            elif i in p:
                if not res or p[i]!=res.pop():
                    return False
        return not res