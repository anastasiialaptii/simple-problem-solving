class Solution(object):
    def firstUniqChar(self, s):
        freq={}
        for char in s:
            freq[char]=freq.get(char,0)+1

        for i, char in enumerate(s):
            if freq[char] == 1:
                return i 

        return -1
        """
        :type s: str
        :rtype: int
        """
        