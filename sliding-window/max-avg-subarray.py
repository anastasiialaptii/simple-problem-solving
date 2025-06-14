class Solution(object):
    def findMaxAverage(self, nums, k):
        left=0
        ksum=0
        res=float('-inf')

        for right, num in enumerate(nums):
            ksum+=num

            if right - left + 1 == k:
                res = max(res, ksum)
                
                ksum -= nums[left]
                left += 1

        return res/float(k)

        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        