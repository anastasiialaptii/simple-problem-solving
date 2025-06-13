class Solution(object):
    def twoSum(self, nums, target):
        seen={}

        for i, num in enumerate(nums):
            res=target-num
            if res in seen:
                return [seen[res],i]
            seen[num]=i
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        