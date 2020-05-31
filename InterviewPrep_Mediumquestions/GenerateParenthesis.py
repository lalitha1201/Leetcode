https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/794/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        results = []
        
        def dfs(r,left,right):
            
            if len(r) == 2 * n:
                
                results.append(r)
                
                return 
            
            if left < n :
                
                dfs(r+'(',left+1,right)
            
            if left > right:
                
                dfs(r+')',left,right+1)
        
        
        dfs('',0,0)
        
        return results
        
