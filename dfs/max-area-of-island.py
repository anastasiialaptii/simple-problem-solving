class Solution(object):
    def dfs(self, matrix, x, y):
        if (x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0])):
          return 0
        if (matrix[x][y] == 0):
          return 0

        matrix[x][y]=0

        area=1
        area+=self.dfs(matrix,x+1,y)
        area+=self.dfs(matrix,x-1,y)
        area+=self.dfs(matrix,x,y+1)
        area+=self.dfs(matrix,x,y-1)
        
        return area


    def maxAreaOfIsland(self, grid):
        cols=len(grid)
        rows=len(grid[0])
        max_area = 0
        arr=[]

        for i in range(cols):
            for j in range(rows):
                if grid[i][j]==1:
                    area=self.dfs(grid,i,j)
                    max_area = max(max_area, area)
        
        return max_area

        """
        :type grid: List[List[int]]
        :rtype: int
        """
        