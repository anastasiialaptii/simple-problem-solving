class Solution(object):
    def maxFreqSum(self, s):
        vowels=['a','e','i','o','u']
        freq_v={}
        freq_c={}

        for char in s:
            if char in vowels:
                freq_v[char] = freq_v.get(char,0)+1
            else:
                freq_c[char] = freq_c.get(char,0)+1
        
        max_v=max(freq_v.values(), default=0)
        max_c=max(freq_c.values(), default=0)

        return max_v+max_c
        """
        :type s: str
        :rtype: int
        """
        