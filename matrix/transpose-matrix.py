class Solution(object):
    def transpose(self, matrix):
        # list comprehenion
        return [[item[i] for item in matrix] for i in range(len(matrix[0]))]

            
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        