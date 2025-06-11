class Solution(object):
    def searchMatrix(self, matrix, target):
        for item in matrix:
            left=0
            right=len(item)-1
            while left<=right:
                midIdx=(left+right)//2
                if item[midIdx]==target:
                    return True
                elif item[midIdx]<target:
                    left=midIdx+1
                else:
                    right=midIdx-1
                
        return False
        