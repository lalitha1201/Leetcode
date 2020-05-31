# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/792/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_num = 0
        if grid == []:
            return island_num
        x_length = len(grid)
        y_length = len(grid[0])
        
        def resetCurIsland(grid, i, j):
            if grid[i][j] == "0":
                return grid
            else:
               grid[i][j] = "0"
                
            if i + 1 < x_length:
                grid = resetCurIsland(grid, i+1, j)
            if j + 1 < y_length:
                grid = resetCurIsland(grid, i, j+1)
            if i - 1 > -1:
                grid = resetCurIsland(grid, i-1, j)
            if j - 1 > -1:
                grid = resetCurIsland(grid, i, j-1)
            return grid
        
        for i in range(x_length):
            for j in range(y_length):
                if grid[i][j] == '1':
                    island_num += 1
                    grid = resetCurIsland(grid, i, j)
        
        return island_num
                    

            
            
