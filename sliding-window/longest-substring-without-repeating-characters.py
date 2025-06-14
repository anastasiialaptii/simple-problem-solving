class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        freq=defaultdict(int)
        max_len=0

        for right, char in enumerate(s):
            freq[char]+=1

            while freq[char] > 1:
                leftChar = s[left]
                freq[leftChar] -= 1
                if freq[leftChar] == 0:
                    del freq[leftChar]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

        """
        :type s: str
        :rtype: int
        """
        