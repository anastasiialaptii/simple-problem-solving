class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        freq_ransom={}
        freq_magazine={}

        for char in ransomNote:
            freq_ransom[char]=freq_ransom.get(char,0)+1

        for char in magazine:
            freq_magazine[char]=freq_magazine.get(char,0)+1

        for key, value in freq_ransom.items():
            if freq_magazine.get(key, 0) < value:  
                return False

        return True              
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        