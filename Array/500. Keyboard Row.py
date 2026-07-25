class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result=[]
        rows=[
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]
        for i in words:
            for j in rows:
                if all([x in j for x in i.lower()]):
                    result.append(i)

        return result