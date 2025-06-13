class Solution(object):
    def containsDuplicate(self, nums):
        freq_nums={}
        
        for num in nums:
            freq_nums[num] = freq_nums.get(num,0)+1

        for value in freq_nums.values():
            if value>1:
                return True
        return False   

        """
        :type nums: List[int]
        :rtype: bool
        """
        