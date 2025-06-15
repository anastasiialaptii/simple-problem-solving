class Solution(object):
    def maxSubArray(self, arr):
        res=maxEnd=float('-inf')

        for i in range(len(arr)):
            maxEnd=max(maxEnd+arr[i], arr[i])
            res=max(maxEnd, res)

        return res


        """
        :type nums: List[int]
        :rtype: int
        """
        