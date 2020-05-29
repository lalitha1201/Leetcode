class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
        
        # padding one dummy -1 to represent empty list
        A = [ -1 ] + A
        B = [ -1 ] + B
        
        m, n = len(A), len(B)
        dp = [ [ 0 for _ in range(n) ] for _ in range(m) ]
        
        
        
        for y in range(1, m):
            for x in range(1, n):
                
                if A[y] == B[x]:
                    # current number is matched, add one more uncrossed line
                    dp[y][x] = dp[y-1][x-1] + 1
                    
                else:
                    # cuurent number is not matched, backtracking to find maximal uncrossed line
                    dp[y][x] = max( dp[y][x-1], dp[y-1][x] )

                    
        return dp[-1][-1]
        
            
                        
                        
                    
        
