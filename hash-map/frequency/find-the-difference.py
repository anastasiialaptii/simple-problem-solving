class Solution(object):
    def findTheDifference(self, s, t):
        freq_s={}
        freq_t={}

        for char in s:
            freq_s[char]=freq_s.get(char, 0)+1

        for char in t:
            freq_t[char]=freq_t.get(char, 0)+1
        
        for key, value in freq_t.items():
            if freq_s.get(key, 0) != value:
                return key
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        