class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board or not board[0]:
            return
        
        m = len(board)
        n = len(board[0])
        
        def dfs(x,y):
            
            if x < 0 or y < 0 or x >= m or y >= n or board[x][y] != 'O':
                
                return
            board[x][y] = 'Z'
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x, y+1)
        
        for j in range(n):
            
            dfs(0, j)
            dfs(m-1, j)
        for i in range(m):
            dfs(i,0)
            dfs(i, n-1)
            
        for x in range(m):
            for y in range(n):
                
                if board[x][y] == 'Z':
                    
                    board[x][y] = 'O'
                else:
                    board[x][y] = 'X'
    
        
    
        
    
