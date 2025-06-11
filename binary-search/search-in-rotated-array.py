class Solution(object):
    def search(self, nums, target):
        left=0
        right=len(nums)-1
        while left<=right:
            midIdx=(left+right)//2
            if nums[midIdx]==target:
                return midIdx
            if nums[left]<=nums[midIdx]:
                if nums[left]<=target<nums[midIdx]:   
                    right = midIdx-1
                else: 
                    left = midIdx+1
            else:
                if nums[midIdx]<target<=nums[right]:
                    left = midIdx+1
                else: 
                    right = midIdx-1
        return -1
