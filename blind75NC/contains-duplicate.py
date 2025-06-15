class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for i, num in enumerate(nums):
            freq[num]=i

        if len(freq)!=len(nums): return True

        return False   
        