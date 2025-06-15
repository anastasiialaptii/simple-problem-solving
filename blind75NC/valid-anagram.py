class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s={}
        freq_t={}
        
        lenS=len(s)
        lenT=len(t)

        if lenS!=lenT: return False

        for char in s:
            freq_s[char]=freq_s.get(char,0)+1
        
        for char in t:
            freq_t[char]=freq_t.get(char,0)+1
        
        if freq_s!=freq_t: return False

        return True
        