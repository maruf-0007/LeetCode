class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        line=0
        width=0
        strr="abcdefghijklmnopqrstuvwxyz"
        for i in s:
            j=strr.index(i)
            width+=widths[j]
            if width==100:
                line+=1
                width=0
            elif width>100:
                line+=1
                width=widths[j]
        if width==0:
            width=100
            line-=1
        return [line+1, width]