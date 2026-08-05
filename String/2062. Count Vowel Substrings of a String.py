class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        c=0
        v={'a','e','i','o','u'}
        for i in range(len(word)-4):
            for j in range(i+5,len(word)+1):
                if set(word[i:j])==v:
                    c+=1
        return c