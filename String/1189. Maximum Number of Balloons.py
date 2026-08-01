class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        s={
            'b':0,
            'a':0,
            'l':0,
            'o':0,
            'n':0
        }
        for i in text:
            if i in s:
                s[i]+=1
        s['l']//=2
        s['o']//=2
        return min(s.values())