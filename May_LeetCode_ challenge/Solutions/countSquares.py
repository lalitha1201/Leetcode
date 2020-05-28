class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        
        m = len(matrix)
        
        n = len(matrix[0])
        
        sum_square = 0
        
        dp = [[0 for x in range(n)] for x in range(m)]
        
        
        for i in range(m):
            
            for j in range(n):
                
                if i == 0 or j == 0:
                    
                    dp[i][j] = matrix[i][j]
                    
                
                elif matrix[i][j] == 1:
                        
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                
                
                sum_square += dp[i][j]
        
        
        return sum_square
