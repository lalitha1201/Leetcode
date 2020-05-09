class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0]*m for _ in range(n)]
        
        # First calculate sum of first row
        cur_sum = grid[0][0]
        for i in range(1,n):
            grid[0][i] = grid[0][i] + cur_sum
            cur_sum = grid[0][i]
        # Calculate sum of first column
        cur_sum = grid[0][0]
        for i in range(1,m):
            grid[i][0] = grid[i][0] + cur_sum
            cur_sum = grid[i][0]
        
        #calculate for rest
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i][j] + min(grid[i][j-1],grid[i-1][j])
        
        return grid[-1][-1]
        
        
        
        
            
