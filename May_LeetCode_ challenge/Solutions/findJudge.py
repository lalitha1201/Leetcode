class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        
        
        town_judge = [0] * (N + 1)
        
        if N == 1:
            
            return N
        
        
        for pair in trust:
            
            town_judge[pair[1]] += 1
            
            town_judge[pair[0]] -= 1
            
        
        
        for i,count in enumerate(town_judge):
            
            if count == N - 1:
                
                return i
            
        return -1
            
            
        
