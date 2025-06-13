class Solution(object):
    def searchInsert(self, nums, target):
        left=0
        right=len(nums)-1

        possibleL=0

        while left<=right:
            midIdx=(left+right)//2
            if target==nums[midIdx]:
                return midIdx
            elif nums[midIdx]<target: 
                left=midIdx+1
                possibleL=left
            else: 
                right=right-1            

        return possibleL


        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        