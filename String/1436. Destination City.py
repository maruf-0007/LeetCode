class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        s=set()
        d=set()
        for i in paths:
            s.add(i[0])
            d.add(i[1])

        return list(d-s)[0]