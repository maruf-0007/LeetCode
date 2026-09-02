class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        st=[]
        for i in s:
            if st and st[-1]+i in ('AB','CD'):
                st.pop()
            else:
                st.append(i)
        return len(st)