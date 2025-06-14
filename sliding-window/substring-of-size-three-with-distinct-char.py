class Solution(object):
    def countGoodSubstrings(self, s):
        left=0
        counter=0
        k=3

        freq=defaultdict(int)

        for right, char in enumerate(s):
            freq[char]+=1

            if right-left+1>k:
                leftChar=s[left]
                freq[leftChar]-=1

                if freq[leftChar]==0:
                    del freq[leftChar]
                left+=1

            if right-left+1==k and len(freq)==k:
                counter+=1
        
        return counter

        """
        :type s: str
        :rtype: int
        """
        